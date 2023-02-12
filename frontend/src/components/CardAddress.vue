<template>
    <div class="address">
        <div class="content">
            <span>CEP: {{ address.cep }}</span>
            <span>Logradouro: {{ address.logradouro }}</span>
            <span>UF: {{ address.uf }}</span>
        </div>
        <button @click="createZipcode(address)">+</button>
    </div>
</template>
<script setup>
import { defineProps, defineEmits } from 'vue'
import api from "../services/api"


const emit = defineEmits(['updateAddresses'])
const props = defineProps(['address'])

async function createZipcode(address) {
    await api.post("/cep", address);
    emit('updateAddresses')
}
</script>

<style scoped>
.address {
    display: flex;
    width: 40%;
    height: 90%;
    border: 1px solid gray;
    border-radius: 0.8rem;
    padding: 2rem;
    margin: 0;
    align-items: center;
}

.address button {
    width: 2rem;
    height: 2rem;
    margin: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;

}

.content {
    display: flex;
    flex-direction: column;
    width: 90%;
    text-align: left;

}
</style>
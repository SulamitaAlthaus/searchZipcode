<template>
    <div class="modal">
        <div class="containerModal">
            <button @click="closeModal" class="close">X</button>
            <h2>Editar CEP</h2>
            <div class="content">
                <div>
                    <label for="">CEP:
                    </label>
                    <input type="text" v-model="address.cep">
                    <label for="">Logradouro:
                    </label>
                    <input type="text" v-model="address.logradouro">
                </div>
                <div>
                    <label for="">Complemento:
                    </label>
                    <input type="text" v-model="address.complemento">
                    <label for="">Bairro:
                    </label>
                    <input type="text" v-model="address.bairro">
                </div>
                <div>
                    <label for="">Localidade:
                    </label>
                    <input type="text" v-model="address.localidade">
                    <label for="">UF:
                    </label>
                    <input type="text" v-model="address.uf">
                </div>
                <div>
                    <label for="">IBGE:
                    </label>
                    <input type="text" v-model="address.ibge">
                    <label for="">GIA:
                    </label>
                    <input type="text" v-model="address.gia">
                </div>
                <label for="">DDD:
                </label>
                <input type="text" v-model="address.ddd">
                <label for="">SIAFI:
                </label>
                <input type="text" v-model="address.siafi">
            </div>
            <div class="saveButton">
                <button @click="saveAddress(address.id)">SALVAR</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import api from "../services/api";

const props = defineProps(['address'])
const emit = defineEmits(['isClose'])

function closeModal() {
    emit('isClose', false)
}

async function saveAddress(id) {
    await api.put(`/cep/${id}`, props.address)
    emit('isClose', false)
}

</script>

<style scoped>
.modal {
    width: 100vw;
    height: 100vh;
    display: block;
    background-color: rgba(108, 108, 108, 0.509);
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
}

.close {
    height: 2rem;
    width: 2rem;
    cursor: pointer;
    float: right;
    display: flex;
    justify-content: center;
    align-items: center;
}

.containerModal {
    height: 60%;
    width: 80%;
    background-color: #242424;
    margin: 4rem auto;
    border-radius: 0.8rem;
    padding: 2rem;
}

.content {
    width: 80%;
    display: block;
    justify-content: center;
    margin: auto;
    line-height: 2rem;
    text-align: left;
    justify-content: center;
    padding: 2rem 4rem;
}

.containerModal h2 {
    text-align: center;
}


.content label {
    margin: 0.5rem;
}

.content label {
    margin: 0.5rem;
}

.saveButton {
    margin: auto;
    padding: 4rem;
    float: right;
}
</style>
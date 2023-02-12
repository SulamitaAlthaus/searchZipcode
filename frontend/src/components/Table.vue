<template>
    <div class="tableHeader">
        <span id="tableColumnTitle">CEP</span>
        <span id="tableColumnTitle">BAIRRO</span>
        <span id="tableColumnTitle">LOCALIDADE</span>
        <span id="tableColumnTitle">UF</span>
        <span id="tableColumnTitle">DDD</span>
        <span id="tableColumnTitle">REDE LOJACORR</span>
        <span id="tableColumnTitle">ACTIONS</span>
    </div>
    <div class="tableCell" v-for="address in addresses">
        <span id="tableCellContent">{{ address.cep }}</span>
        <span id="tableCellContent">{{ address.bairro }}</span>
        <span id="tableCellContent">{{ address.localidade }}</span>
        <span id="tableCellContent">{{ address.uf }}</span>
        <span id="tableCellContent">{{ address.ddd }}</span>
        <span id="tableCellContent">
            <input type="checkbox" :checked="address.lojacorr" disabled />
        </span>
        <span id="actionsButtons">
            <button @click="obj.isOpen = true, obj.address = address">
                <img id="icon" src='../assets/edit.png' alt="Edit">
            </button>
            <button @click="removeAddrress(address.id)">
                <img id="icon" src='../assets/remove.png' alt="Remove">
            </button>
        </span>
    </div>
    <Modal v-if="obj.isOpen" :address="obj.address" @isClose="closeModal" />
</template>
<script setup>
import { defineProps, defineEmits, reactive } from 'vue'
import api from "../services/api"
import Modal from "../components/Modal.vue"

const props = defineProps(['addresses'])
const emit = defineEmits(['updateAddresses'])

const obj = reactive({
    isOpen: false,
    address: {}
})

async function removeAddrress(id) {
    await api.delete(`/cep/${id}`);
    emit('updateAddresses')
}
function closeModal() {
    obj.isOpen = false
}
</script>

<style scoped>
.tableHeader {
    font-weight: bold;
    width: 100%;
    height: 2rem;
    padding: 2rem 0;
    display: flex;
    justify-content: space-around;
}

.tableCell {
    width: 100%;
    min-height: 2rem;
    display: flex;
    justify-content: space-around;
    margin: 0.2rem;
}

#tableColumnTitle,
#tableCellContent {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.2rem;
    width: 10rem;
}

#icon {
    height: 1rem;
    filter: invert(75%);
}

#actionsButtons {
    display: flex;
    width: 10rem;
    padding: 0.2rem;
    align-items: center;
    justify-content: center;
    min-height: 2rem;
}

#actionsButtons button {
    height: 2rem;
    width: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0.2rem;
}
</style>
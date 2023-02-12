<template>
    <div class="container">
        <div class="searchArea">
            <SearchZipcode @address="getAddress" />
            <CardAddress v-if="obj.address" :address="obj.address" @updateAddresses="getAddresses" />
        </div>
        <div class="table" v-if="obj.openTable">
            <Table :addresses=obj.addresses @updateAddresses="getAddresses" />
        </div>
    </div>
</template>

<script setup>
import { reactive, onMounted } from "vue"
import api from "../services/api"
import Table from "../components/Table.vue"
import SearchZipcode from "../components/SearchZipcode.vue"
import CardAddress from "../components/CardAddress.vue"

const obj = reactive({
    address: '',
    addresses: [],
    openTable: false
})

onMounted(() => {
    getAddresses()
})

async function getAddress(address) {
    obj.address = address
}

async function getAddresses() {
    const response = await api.get("/cep");
    obj.addresses = response.data;
    if (obj.addresses.length > 0) {
        obj.openTable = true
    } else {
        obj.openTable = false
    }
}

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}


.searchArea {
    display: flex;
    align-items: center;
    justify-content: start;
    gap: 4rem;
    height: 10vh;
    margin: 2rem 0;
    width: 90vw;
}

.table {
    width: 90vw;
    margin-top: 2rem;
    border: 1px solid gray;
    border-radius: 0.8rem;
    text-align: left;
    justify-content: space-between;
}
</style>
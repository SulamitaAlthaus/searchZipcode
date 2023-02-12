<template>
    <div class="container">
        <div class="search">
            <label for="">Digite o CEP: </label>
            <input type="text" v-model="zipcode">
        </div>
        <button @click="searchZipcode(zipcode)">Search</button>
        <div v-if="obj.address" class="contentContainer">
            <div class="content">
                <span>CEP: {{ obj.address.cep }}</span>
                <span>Logradouro: {{ obj.address.logradouro }}</span>
                <span>UF: {{ obj.address.uf }}</span>
            </div>
                <button @click="createZipcode(obj.address)">+</button>
        </div>
        <div class="table" v-if="obj.addresses">
            <Table :addresses=obj.addresses @updateAddresses="getAddresses"/>
        </div>
    </div>
</template>

<script setup>
    import { reactive, onMounted } from "vue"
    import api from "../services/api"
    import Table from "../components/Table.vue"

    let zipcode

    const obj = reactive({
        address: '',
        addresses: []
    })

    onMounted(() => {
       getAddresses()
    })

    async function searchZipcode(zipcode) {
        zipcode = zipcode.replace(/[^0-9]/g, '');
        try {
            const response = await fetch(`https://viacep.com.br/ws/${zipcode}/json/`)
            obj.address = await response.json()
        } catch (err) {
            console.error(err)
        }
    }
    async function getAddresses() {
        const response = await api.get("/cep");
        console.log("response", response)
        obj.addresses = response.data;
    }

    async function createZipcode(address) {
        await api.post("/cep", address);
        getAddresses()
    }

</script>

<style scoped>
.container{
    display: flex;
    flex-direction: column;
}
.search{
    padding: 8px 0;
}
.contentContainer{
    display: flex;
}
.contentContainer button{
    width: 2rem;
    height: 2rem;
    margin: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
}
.content{
    display: flex;
    flex-direction: column;
    padding: 16px 0;
    text-align: left;
}
.table{
    width: 90vw;
    margin-top: 4rem;
    border: 1px solid gray;
    text-align: left;
    justify-content: space-between;
}
.tableHeader{
    font-weight: bold;
    width: 100%;
    height: 2rem;
    display: flex;
    justify-content: space-between;
}
#tableColumnTitle{
    padding: 0 2rem;
    width: 10%;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid gray;
}
.tableCell{
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-around;
    border: 1px solid gray;
    text-align: center;

}
#tableCellContent{
    width: 10%;
    padding: 0.2rem ;

}
</style>
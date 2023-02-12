<template>
    <div class="modal">
        <div class="container">
            <button @click="isClose()" class="close" >X</button>
            <div class="content">
                <h2>Editar CEP</h2>
                <label for="">CEP: 
                    <input type="text" :v-model="obj.addressUpdate.cep" :defaultValue="address.cep">
                </label>
                <label for="">Logradouro: 
                    <input type="text" :v-model="obj.addressUpdate.logradouro" :defaultValue="address.logradouro">
                </label>
                <label for="">Complemento: 
                    <input type="text" :v-model="obj.addressUpdate.complemento" :defaultValue="address.complemento">
                </label>
                <label for="">Bairro: 
                    <input type="text" :v-model="obj.addressUpdate.bairro" :defaultValue="address.bairro">
                </label>
                <label for="">Localidade: 
                    <input type="text" :v-model="obj.addressUpdate.localidade" :defaultValue="address.localidade">
                </label>
                <label for="">UF: 
                    <input type="text" :v-model="obj.addressUpdate.uf" :defaultValue="address.uf">
                </label>
                <label for="">IBGE: 
                    <input type="text" :v-model="obj.addressUpdate.ibge" :defaultValue="address.ibge">
                </label>
                <label for="">GIA: 
                    <input type="text" :v-model="obj.addressUpdate.gia" :defaultValue="address.gia">
                </label>
                <label for="">DDD: 
                    <input type="text" :v-model="obj.addressUpdate.ddd" :defaultValue="address.ddd">
                </label>
                <label for="">SIAFI: 
                    <input type="text" :v-model="obj.addressUpdate.siafi" :defaultValue="address.siafi">
                </label>

                <button @click="saveAddress(address.id)">SALVAR</button>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { defineProps, defineEmits, reactive } from "vue";
    import api from "../services/api";

    const props = defineProps(['address'])
    const emit = defineEmits(['isClose'])

    const obj = reactive({
        addressUpdate: {}
    })

    function isClose() {
        emit('isClose')
    }

async function saveAddress(id) {
        console.log(obj.addressUpdate)
        await api.put(`/cep/${id}`, obj.addressUpdate);
        emit('isClose')        
    }

</script>

<style scoped>
.modal{
    width: 100vw;
    height: 100vh;
    display: block; 
    background-color: rgba(108, 108, 108, 0.509);
    position: fixed; 
    z-index: 1; 
    left: 0;
    top: 0;
}
.close{
    height: 2rem;
    width: 2rem;
    cursor:pointer;
    float: right;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container{
    height: 80%;
    width: 80%;
    background-color: #242424;
    margin: 4rem auto;
    padding: 2rem;
}
.content{
    width: 80%;
    display: flex;
    flex-direction: column;
    padding: 0 4rem;
    gap: 0.5rem;
    text-align: left;
}
.content h2{
    text-align: center;
}
</style>
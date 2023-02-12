<template>
    <div class="search">
        <div>
            <label for="search">Digite o CEP: </label>
            <input id="search" type="text" v-model="obj.zipcode">
        </div>
        <button @click="searchZipcode(obj.zipcode)">Search</button>
    </div>
</template>

<script setup>

import { defineEmits, reactive } from 'vue'

const emit = defineEmits(['address'])

const obj = reactive({
    address: '',
    zipcode: ''
})

async function searchZipcode(zipcode) {
    zipcode = zipcode.replace(/[^0-9]/g, '');
    try {
        const response = await fetch(`https://viacep.com.br/ws/${zipcode}/json/`)
        emit('address', await response.json())
    } catch (err) {
        console.error(err)
    }
}
</script>

<style scoped>
.search {
    display: flex;
    width: 40vw;
    height: 90%;
    border: 1px solid gray;
    border-radius: 0.8rem;
    padding: 2rem;
    margin: 0;
    align-items: center;
}
</style>

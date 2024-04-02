<script>
    export default {
        props: {
            Question : Object
        },
        methods:{
            remove: function(){
                this.$emit('remove', this.Question);
            },
            modifier: function(){
                this.$emit('modifier', this.Question);
            }
        },
        emits: ['remove', 'modifier']
    }
</script>

<template>
    <div>
        <h2>{{Question.title}}</h2>
        <h3>Choix disponibles :</h3>
        <div>
            <label>Choix 1:</label>
            <input disabled v-model="Question.choix1">
            <label>Choix 2:</label>
            <input disabled v-model="Question.choix2">
            <div v-if="Question.choix3">
                <label>Choix 3:</label>
                <input  disabled v-model="Question.choix3">
            </div>
            <div v-if="Question.choix4">
                <label>Choix 4:</label>
                <input disabled v-model="Question.choix4">
            </div>
        </div>
        <button @click="remove">Remove</button>
        <button @click="modifier">Modifier</button>
    </div>
</template>


<script>

export default {
    props: {
        questionnaire: Object
    },
    methods: {

        remove() {
            this.$emit('remove', this.questionnaire)
        },
        modifier: function() {
            this.$emit('modifier', this.questionnaire)
        }
    },
    emits: ['remove']
}
</script>

<template>
    <h2>Questionnaire : {{  this.questionnaire.nom  }}</h2>
    <li>
        <div class="checkbox" v-bind:class="{ 'alert alert-success': todo.checked}">
            <input type="checkbox" v-model="todo.checked"></input>
            {{ todo.text }}
            <button @click = "remove">Supprimer</button>
            <button @click = "modifier">Modifier</button>
        </div>
    </li>
</template>
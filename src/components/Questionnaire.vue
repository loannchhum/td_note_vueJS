<script>

export default {
    props: {
        Questionnaire: Object
    },
    methods: {

        remove() {
            this.$emit('remove', this.Questionnaire)
        },
        modifier: function() {
            this.$emit('modifier', this.Questionnaire)
        },
        showQuestions() {
            this.$emit('showQuestions', this.Questionnaire.id);
        }
    },
    emits: ['remove', 'modifier', 'showQuestions']
}
</script>

<template>
    <h2 @click="showQuestions">{{Questionnaire.name}}</h2>
    <li>
        <div>
            <button @click = "remove">Supprimer</button>
            <button @click = "modifier">Modifier</button>
            
        </div>
    </li>
</template>
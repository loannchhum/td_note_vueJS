<script>
import Question from './Question.vue';

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
        }
    },
    emits: ['remove'],
    components : { Question }
}
</script>

<template>
    <h3>Questionnaire : {{  this.Questionnaire.nom  }}</h3>
    <li>
        <div>
            {{ Questionnaire.text }}
            <button @click = "remove">Supprimer</button>
            <button @click = "modifier">Modifier</button>
            <Question v-for="question in questions" :question="question" @afficherQuestion="afficherQuestion(question.id)"></Question>
        </div>
    </li>
</template>
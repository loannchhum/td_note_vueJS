<script>
import Question from './Question.vue';
import axios from 'axios'


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
    {{  this.Questionnaire.nom  }}
    <li>
        <div>
            {{ Questionnaire.text }}
            <button @click = "remove">Supprimer</button>
            <button @click = "modifier">Modifier</button>
            <Question v-for="question in questions" :question="question" @afficherQuestion="afficherQuestion(question.id)"></Question>
        </div>
    </li>
</template>
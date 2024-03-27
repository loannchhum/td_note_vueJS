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
        }
    },
    emits: ['remove', 'modifier']
}
</script>

<template>
    <h3>{{  this.Questionnaire.name  }}</h3>
    <li>
        <div>
            <button @click = "remove">Supprimer</button>
            <button @click = "modifier">Modifier</button>
        </div>
    </li>
</template>
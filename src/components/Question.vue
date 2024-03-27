<script>
    export default {
        props: {
            Question : Object
        },
        methods:{
            remove: function(){
                this.$emit('remove', this.Question.id);
            },
            modifier: function(){
                this.$emit('modifier', this.Question.id);
            }
        },
        emits: ['remove']
    }
</script>

<template>
    <div>
    <label>
        <input type="radio" name="question" :value="Question.id" @change="modifier">
        {{Question.question}}
        <button @click="$emit('remove', Question.id)">Remove</button>
        <button @click="modifier">Modifier</button>
    </label>
    
    </div>
</template>

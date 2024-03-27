<script>
import Questionnaire from './components/Questionnaire.vue'

export default {
  name: 'App',
  methods:{
    AfficherQuestionnaire(id){

    },
    creerQuestionnaire(){

    },

    supprimerQuestionnaire(){

    },

    modifierQuestionnaire(){

    }
  },

  components: { Questionnaire }
}

</script>

<template>
  <body>
    <h1>Application </h1>
    <img class="images" src="/img/10738849-autocollant-d-un-signe-de-quiz-de-dessin-anime-vectoriel.jpg">
    <ul>
      <p>Vous pouvez répondre aux questionnaires comportant plusieurs types de questions,
        avec réponse simple et avec réponses multiples.</p>
      <h2>Questionnaires disponibles :</h2>
      <Questionnaire v-for="questionnaire in questionnaires" :questionnaire="questionnaire" @AfficherQuestionnaire="afficherQuestionnaire(questionnaire.id)"/>
    </ul>


  </body>
</template>

<style>
html{
  flex-wrap: wrap;

}
body {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.images{
  height: 10vh;
}

</style>

<script>
import Questionnaire from './components/Questionnaire.vue'
import axios from 'axios'

let data= {
  questionnaires: []
}

export default {
  name: 'App',
  data(){
    return data;
  },

  mounted(){
    this.loadDB();
  },

  methods:{
    async loadDB(){

      const response = await axios.get('http://localhost:5000/');
      // on enregistre les données dans let data
      console.log(response.data)
    },

    afficherTousLesQuestionnaires(){
      this.questionnaires.forEach(questionnaire => {
        console.log(questionnaire);
      });
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
    <Questionnaire v-for="questionnaire in questionnaires" :questionnaire="questionnaire" />
    
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

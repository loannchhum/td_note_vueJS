<script>
import Questionnaire from './components/Questionnaire.vue'
import Question from './components/Question.vue'
import axios from 'axios'

const data = {
  questionnaires:[],
}

const quest = {
  questions:[],
}

export default {
  name: 'App',
  data(){
    return {
      questionnaires: [],
      questions: [],
      questionAModifier: null,
      creerQuestion: false,
      questionnaireAuquelOnAjouteUneQueestion:null

    }
  },

  mounted(){
    this.loadDB();
  },

  methods:{
    async loadDB(){

      const response = await axios.get('http://localhost:5000/quiz/api/v1.0/questionnaire');
      this.questionnaires = this.mapper(response.data.questionnaires);
      this.questions = [];
      this.questionAModifier = null;
      this.questionnaireAModifier = null;
      this.questionnaireAuquelOnAjouteUneQueestion=null;
      this.creerQuestion = false;
    },
    mapper(questionnaires){
      return questionnaires.map(questionnaire => {
        return {
          id: questionnaire.id,
          name: questionnaire.name
        }
      })
    },
    // afficher un formulaire pour crée un nouveau questionnaire
    async creerQuestionnaire(){
      const response = await axios.post('http://localhost:5000/quiz/api/v1.0/questionnaire', {name: this.name});
      if(response.status === 201){
        console.log(response.data.id)
        this.questionnaires.push({
          id: response.data.id,
          name: this.name
        });
        this.name = '';
      }
      else{
        alert('Erreur lors de la création du questionnaire');
      }
    },

    async supprimerQuestionnaire(questionnaire){
      console.log(questionnaire.name, questionnaire.id);
      const supprime=await axios.delete(`http://localhost:5000/quiz/api/v1.0/questionnaire/${questionnaire.id}`);
      if(supprime.status === 200){
        this.questionnaires = this.questionnaires.filter(q => q.id !== questionnaire.id);
      }

    },

    async modifQuestionnaire(questionnaire){
      const response = await axios.put(`http://localhost:5000/quiz/api/v1.0/questionnaire/${questionnaire.id}`, questionnaire);
      if(response.status === 200){
        this.questionnaires = this.questionnaires.map(q => {
          if(q.id === questionnaire.id){
            return questionnaire;
          }
          return q;
        });
      }
    },
    // formulaire de modification d'un questionnaire
    modifierQuestionnaire(questionnaire){
      const name = prompt('Entrez le nouveau nom du questionnaire');
      if(name){
        questionnaire.name = name;
        this.modifQuestionnaire(questionnaire);
      }
    },
    async displayQuestions(questionnaire){
      this.questionnaireAModifier = true;
      console.log(questionnaire.id);
      const response = await axios.get(`http://localhost:5000/quiz/api/v1.0/questionnaire/${questionnaire.id}`);
      // suppresion des questionnaire pour afficher les questions

      this.questionnaireAuquelOnAjouteUneQueestion=this.questionnaires.filter(q => q.id === questionnaire.id);
      this.questionnaires = [];
      this.questions = response.data.questions;
      console.log(this.questions);
    },

  
    async supprimerQuestion(question){
      const supprime=await axios.delete(`http://localhost:5000/quiz/api/v1.0/questionnaire/question/${question.id}`);
      if(supprime.status === 200){
        this.questions = this.questions.filter(q => q.id !== question.id);
      }
    },

    async afficherFormulaireModificationQuestion(question){
      
      this.questionAModifier = question;
    },
    async modifierQuestion(){
      console.log(this.questionAModifier);
      const response = await axios.put(`http://localhost:5000/quiz/api/v1.0/questionnaire/question/${this.questionAModifier.id}`, this.questionAModifier);
      if(response.status === 200){
        this.questions = this.questions.map(q => {
          if(q.id === this.questionAModifier.id){
            return this.questionAModifier;
          }
          return q;
        });
        this.questionAModifier = null;
      }
    },
    afficherFormulaireCreeQuest() {
      this.questionAModifier = null; // Assurez-vous que le formulaire de modification soit caché
      this.creerQuestion = true; // Affichez le formulaire de création de question
    },

  
    async creerQuest() {
      let ques= {
        title: document.getElementById('nomq').value,
        reponse: document.getElementById('repq').value,
        questionnaire_id: this.questionnaireAuquelOnAjouteUneQueestion[0].id
      }
      if (ques.title === '' || ques.reponse === '' || ques.choix1 === '' || ques.choix2 === '' ) {
        alert('Veuillez remplir tous les champs');
        return;
      }
      let choix1 = document.getElementById('c1q').value;
      let choix2 = document.getElementById('c2q').value;
      let choix3 = document.getElementById('c3q').value;
      let choix4 = document.getElementById('c4q').value;
      console.log(choix3, choix4);
      if (choix1 === '' || choix2 === '') {
        alert('Veuillez remplir les deux premiers choix');
        return;
      }
      else{
        ques.choix1 = choix1;
        ques.choix2 = choix2;
      }

      if (choix3 !== '' && choix4 == '') {
        alert('Veuillez remplir le derniers choix');
        return;
      }
      else if (choix3 == '' && choix4 !== '') {
        alert('Veuillez remplir le troisième choix');
        return;
      }
      else if (choix3 !== '' && choix4 !== '') {
        ques.choix3 = choix3;
        ques.choix4 = choix4;
      }
    
      const response = await axios.post('http://localhost:5000/quiz/api/v1.0/questionnaire/question', ques);
        console.log('tetetete')
        console.log(response.data.questions);
        this.questions.push(response.data.questions);
        // Cachez le formulaire de création de question
        this.creerQuestion = false;
      
    },
  },


  components: { Questionnaire, Question}
}

</script>

<template>
  <body>
    <div class="conteneur" @click="loadDB()">
      <h1>Application</h1>
      <img class="images" src="/img/10738849-autocollant-d-un-signe-de-quiz-de-dessin-anime-vectoriel.jpg">
    </div>
    <div v-if="this.questionnaireAModifier == null">
          <input type="text" v-model="name" placeholder="Nom du questionnaire">
          <button @click="creerQuestionnaire">Créer un questionnaire</button>
    </div>
      
       <!-- afficher chacun des questionnaires  -->
       <div class="conteneur" >
            <Questionnaire v-for="questionnaire in questionnaires" :Questionnaire="questionnaire" @remove="supprimerQuestionnaire(questionnaire)" @modifier="modifierQuestionnaire(questionnaire)" @showQuestions="displayQuestions(questionnaire)"></Questionnaire>
         
        </div>
        <!-- afficher les questions -->
        <div class="conteneur">
          <button v-if="this.questionnaireAModifier" @click="afficherFormulaireCreeQuest()" >Ajouter une question</button>
            <div v-if="creerQuestion">
              <h2>Créer une question</h2>
              <form @submit.prevent="creerQuest()">
                <label>Nom de la question:</label>
                <input id="nomq" type="text"><br>
                <label>Réponse:</label>
                <input id="repq" type="text"><br>
                <label>Choix 1:</label>
                <input id="c1q" type="text" ><br>
                <label>Choix 2:</label>
                <input id="c2q" type="text" ><br>
                  <label>Choix 3:</label>
                  <input id="c3q" type="text" ><br>
                  <label>Choix 4:</label>
                  <input id="c4q" type="text" ><br>
                
                <button type="submit">Créer</button>
              </form>
            </div>
          <div>

          <Question v-for="question in questions" v-if="questions.length > 0"  :Question="question" @remove="supprimerQuestion(question)" @modifier="afficherFormulaireModificationQuestion(question)"></Question>

          </div>
        </div>
        

        <div v-if="questionAModifier">
          
          <h2>Modifier la question</h2>
          <form @submit.prevent="modifierQuestion()">
            <label>Nom de la question:</label>
            <input type="text" v-model="questionAModifier.title"><br>
            <label>Réponse:</label>
            <input type="text" v-model="questionAModifier.reponse"><br>
            <!-- Ajoutez les champs pour les choix de la question -->
            <!-- Par exemple, pour une question simple -->
            <label>Choix 1:</label>
            <input type="text" v-model="questionAModifier.choix1"><br>
            <label>Choix 2:</label>
            <input type="text" v-model="questionAModifier.choix2"><br>
            <div v-if="questionAModifier.choix3 && questionAModifier.choix4">              <label>Choix 3:</label>
              <input type="text" v-model="questionAModifier.choix3"><br>
              <label>Choix 4:</label>
              <input type="text" v-model="questionAModifier.choix4"><br>
            </div>
            <button type="submit">Modifier</button>
          </form>
        </div>

  </body>
</template>

<style>
html{
  flex-wrap: wrap;

}
.conteneur{
  display: block;
  justify-content: center;
  align-items: center;
}
.images{
  height: 10vh;
}

body > * {
  margin: 3em;
}

</style>
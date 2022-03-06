pipeline {
agent any


stages {

stage('Feature branch deployment, testing') {
  when {
                branch 'feature_branch'
            }

      steps {
        bat 'echo Hello'
        //bat '''
        //echo feature-branch
        //docker-compose build
        //docker-compose up -d

        //cd tests
        //python -m pytest
        // '''

            }
  }


  stage('Feature branch push to develop') {
    when {
                  branch 'feature_branch'
              }

        steps {

        withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                 bat "git branch"
             }

              }
    }



  stage('Git develop') {
    when {
                  branch 'develop'
              }

        steps {

          bat 'echo develop'

              }
            }

  stage('Git master') {
    when {
                  branch 'master'
              }

        steps {

          bat 'echo master'

              }
            }



  }
}

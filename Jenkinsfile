pipeline {
agent any


stages {

stage('Feature branch deployment and testing') {
  when {
                branch 'feature-branch'
            }


      steps {

        bat 'echo feature-branch'

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

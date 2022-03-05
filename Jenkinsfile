pipeline {
agent any


stages {

stage('Git test') {
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

          bat 'echo hello'

              }
            }

  stage('Git master') {
    when {
                  branch 'master'
              }

        steps {

          bat 'echo hello'

              }
            }



  }
}

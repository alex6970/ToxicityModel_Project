pipeline {
agent any


stages {

stage('Git test') {
  when {
                branch 'master'
            }

      steps {

        bat 'git branch'

            }
          }

  stage('Git test2') {
    when {
                  branch 'develop'
              }

        steps {

          bat 'echo hello'

              }
            }



  }
}

pipeline {
agent any


stages {

stage('Feature branch deployment and testing') {
  when {
                branch 'feature-branch'
            }


      steps {

        bat '''echo feature-branch'''
        bat '''docker-compose build'''
        bat '''docker-compose up -d'''

        bat '''cd tests'''
        bat '''python -m pytest'''

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






pipeline {
agent any


stages {



stage('Building') {
      steps {

        bat 'docker-compose build'

            }
          }

stage('Running the container') {
      steps {

        bat 'docker-compose up -d'

            }
          }

  stage('Container down and cleaning') {
        steps {

          bat 'docker-compose down'

              }
            }

  }
}

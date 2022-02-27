pipeline {
agent any

stages {
    stage('Build and Running') {
        steps {

          script{

          if(env.BRANCH_NAME == 'develop'){

            bat 'docker-compose up -d --build'
            // echo 'It works'

          }

          }
        }
    }

    stage('Running tests') {
                steps {

                script{

                if(env.BRANCH_NAME == 'develop'){

                    // add steps to run python tests
                    // cf. jenkins branch selection

                    bat 'cd tests'
                    bat 'python -m pytest'

                }

            }
        }
    }

    stage('Shutting down') {
                steps {

                script{

                if(env.BRANCH_NAME == 'develop'){

                bat 'docker-compose down'


                }

            }

        }
    }

  }
}

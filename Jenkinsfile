pipeline {
agent any

stages {
    stage('Build, running and testing') {
      parallel {
              stage('Running and building') {
                            steps {

                                echo 'this is working aight'

                                bat 'docker-compose up -d --build'
                                // echo 'It works'


                                }
                        }

                stage('Running tests') {
                            steps {

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

                bat 'docker-compose down'
        }
    }

  }
}


// script{

// if(env.BRANCH_NAME == 'develop'){

// bat 'docker-compose down'

// }

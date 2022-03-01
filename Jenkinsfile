pipeline {
agent any
    stages {
        stage('Build and Running') {
            when {
                    branch 'develop'
                }
            steps {
                bat 'docker-compose up --build'
                // echo 'It works'
            }
        }

    }
}

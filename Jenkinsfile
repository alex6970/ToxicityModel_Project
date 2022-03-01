pipeline {
agent any
    stages {
        stage('Build and Running') {
            when {
                    branch 'develop'
                }
            steps {
                bat 'docker-compose up -d --build'
                // echo 'It works'
            }
        }

    }
}

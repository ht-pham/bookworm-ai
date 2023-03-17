pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t chatbox-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run chatbox-app pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 80:5000 chatbox-app'
            }
        }
    }
}




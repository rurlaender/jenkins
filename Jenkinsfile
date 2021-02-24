pipeline {
    agent {label 'python'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 -venv venv'
                sh '. venv/bin/activate'
                sh 'python main.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

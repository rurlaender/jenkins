pipeline {
    agent {label 'python'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
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

pipeline {
    agent {label 'python'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && python main.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'pip install pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

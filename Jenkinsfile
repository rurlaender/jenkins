pipeline {
    agent {label 'python'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'rm -rf venv'
                sh 'python3 -m venv venv'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'rm result.xml'
                sh '. venv/bin/activate && pip install pytest && pytest ./test --junitxml=result.xml'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    post {
        always {
            junit 'result.xml'
        }
    }
}

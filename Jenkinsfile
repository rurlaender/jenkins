pipeline {
    agent {label 'python'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'rm -rf venv'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && python main.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
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

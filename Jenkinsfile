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
                sh 'rm -f result.xml'
                sh '. venv/bin/activate && pip3 install pytest'
                sh 'pytest ./test --junitxml=result.xml'
            }
        }
        stage('Generat documentation') {
            steps {
                sh '. venv/bin/activate && pdoc src --html --force'
                sh 'cp ./html/src/* /home/jenkins/doc'
            }
        }
    }
    post {
        always {
            junit 'result.xml'
        }
    }
}

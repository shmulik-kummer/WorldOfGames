pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'master']],
                    userRemoteConfigs: [[url: 'https://github.com/shmulik-kummer/WorldOfGames.git']]
                ])
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000 -v $(pwd)/Scores.txt:/app/Scores.txt myapp'
            }
        }

        stage('Test') {
            steps {
                wrap([$class: 'Xvfb']) {
                sh 'python3 tests/e2e.py'
        }
    }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop $(docker ps -q --filter ancestor=myapp)'
                sh 'docker tag myapp kummer/myapp'
                sh 'docker login'
                sh 'docker push kummer/myapp'
            }
        }
    }
}

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
                sh 'docker run -d -p 8777:8777 -v $(pwd)/Scores.txt:/app/Scores.txt myapp'
            }
        }

        stage('Test') {
            steps {
                sh 'python tests/e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop $(docker ps -q --filter ancestor=myapp)'
                sh 'docker tag myapp kummer/myapp'
                sh 'docker push kummer/myapp'
            }
        }
    }
}

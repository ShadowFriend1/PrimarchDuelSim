pipeline {
    agent any
    stages {
		stage('SonarQube analysis') {
			environment {
        		scannerHome = tool 'SonarQubeScanner'
    		}    
			steps {
        		withSonarQubeEnv('My SonarQube Server') {
            		sh "${scannerHome}/bin/sonar-scanner"
				}
        	}
		}
		stage('Checkout Git Comment Program') {
			when {
				changeRequest()
			}
			steps {
				git credentialsId: '33be1895-4822-4709-9977-56ae072efd6f', url: 'https://github.com/ShadowFriend1/pr-Decoration.git'
			}
		}
		stage('Post Pull Request Comment') {
			when {
				changeRequest()
			}
			environment {
				goInstallation = tool 'Go:latest'
				SONARQUBEPROJECT = 'my:project'
				REPO = 'PrimarchDuelSim'
				PULL_REQ_NUMBER = env.CHANGE_ID
			}
			steps {
				withSonarQubeEnv('My SonarQube Server') {
            		sh 'export SONARQUBEURL=$SONAR_HOST_URL'
				}
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'my-sonarqube-server-login',
								usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
					sh 'export SONARQUBEUSER=$USERNAME'
					sh 'export SONARQUBEPASSWORD=$PASSWORD'
 				}
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aab572d0-f1d3-4f9b-b930-812bcb49d485',
								usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
					sh 'export OWNER=$USERNAME'
					sh 'export GITHUB_API_KEY=$PASSWORD'
 				}
				withEnv(["GOROOT=${Go:latest}", "PATH+GO=${Go:latest}/bin"]) {
					sh 'go run new.go'
				}
			}
		}
    }
}

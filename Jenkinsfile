pipeline {
    agent any
    stages {
	    stage('Check Versions') {
	        steps {
		        sh '''
		        mvn --version
		        '''
	        }
	    }
		stage('SonarQube analysis') {
			environment {
        		scannerHome = tool 'SonarQubeScanner'
    		}    
			steps {
        		withSonarQubeEnv('sonarqube') {
            		sh "${scannerHome}/bin/sonar-scanner"
        	}
		}
    }
}

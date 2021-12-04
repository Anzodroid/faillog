pipeline {
    agent any
    parameters {
        string(name: 'Greeting', defaultValue: 'Hello Amazing', description: 'How should I greet the world?')
    }

    stages {
        stage('Hello') {
            steps {
                timeout(time: 1, unit: 'MINUTES'){
                echo 'Hello World'
                echo "${params.Greeting} World"
                sh '''
                echo "Hello Shell"
                '''
                }
                
                // powershell '''
                //echo "Hello PowerShell"
                //'''
            }
            
        stage('Run Python Script') {
            steps {
                timeout(time: 1, unit: 'MINUTES'){
                sh '''
                python faillog.py -a test.txt
                '''
                }
                
                // powershell '''
                //echo "Hello PowerShell"
                //'''
            }

        
        }
        
        
    }
}

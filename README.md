# GRG-55

1. Step function state machine is titled GRG-55, here https://eu-west-2.console.aws.amazon.com/states/home?region=eu-west-2#/statemachines
  Here are its details: ![image](https://user-images.githubusercontent.com/43206011/143222021-b39352b6-083d-4ba4-bc6c-4d298eed066d.png)
2. Start execution, using input:
    {
      "SourceBucket": "grg-55-source",
      "SourceObjectKey": "sample.txt",
      "DestinationBucket": "grg-55-dest"
    }
3. In S3, refresh bucket grg-55-dest, the field "Last Modified" should reflect when the step function was last executed. 

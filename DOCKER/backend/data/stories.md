## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## python custom code
* python
  - action_python_custom
  
## Search documentation test
* search_documentation_test
	- action_searchdoc_test
	
* thank
	- utter_noworries
	- utter_further_help
	
	
## Search documentation changes
* search_documentation_changes
	- action_searchdoc_changes
	
## Definition for testings
* testing_definitions
    - action_testing_def
	
	
## name entry test
* greet
	- utter_greet	
* name_entry
	- utter_name_help
	

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye
  
## types of testing
* testing_types
  - utter_testingtypes1
  - utter_testingtypes2
  - utter_testingtypes3
  - utter_testingtypes4
  - utter_testingtypes5
  
  
  

  
## thank deny
* thank
  - utter_noworries
  - utter_further_help
  
* deny
  - utter_goodbye
  - utter_rating
  
## thank accept
* thank
  - utter_noworries
  - utter_further_help
  
* affirm
  -utter_rehelp


## default fallback
* bot_challenge
	- action_default_fallback
 
  
## goodbye
* bye
  - utter_rating

## Final bye
* bye
  - utter_finalbye

## rating_5
* five
  - utter_rating5
  - utter_feedbackyn

## rating_4
* four
  - utter_rating4
  - utter_feedbackyn  
## rating_3
* three
  - utter_rating3
  - utter_feedbackyn
## rating_2
* two
  - utter_rating2
  - utter_feedbackyn
## rating_1
* one
  - utter_rating1  
  - utter_feedbackyn
  
## feedbackyes
* feedbackyes
  - utter_feedbackyes
  
* bye
  - utter_finalbye
  
## feedbackno
* feedbackno
  - utter_feedbackno

  
## bot challenge
* bot_challenge
  - utter_iamabot
  
## some question from testing
* test
  - utter_test
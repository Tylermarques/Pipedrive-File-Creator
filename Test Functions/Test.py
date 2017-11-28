import boto3

def handler(event, context):
    print("Handler begins handling")
    determine_request(event, event["event"])


def determine_request(event, requestType):
    #TODO add cases for calling each function based on event type
    event_switcher = {
        "added.deal": deal_added,
        "updated.deal": deal_updated
    }


def deal_added(event):
    pass


def deal_updated(event):
    #TODO Is it in the main pipeline
    cur_stage = event["current"]["stage_id"]
    prev_stage = event["previous"]["stage_id"]
    if cur_stage == prev_stage:
        print("No stage change detected")
        return
    # Stage 8 is LOI in main pipeline
    if cur_stage == 8:

    stage_switcher= {

    }

def attach_file(id, file):
    #TODO Upload file using api key and pipedrive api
    pass

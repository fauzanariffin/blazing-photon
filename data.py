from datetime import datetime, time

CONFERENCE_INFO = {
    "title": "Google Cloud Tech Day 2025",
    "date": "November 26, 2025",
    "location": "Google Singapore, Mapletree Business City II",
    "description": "Join us for a day of deep dives into Google Cloud technologies, from AI/ML to Serverless and Kubernetes."
}

SPEAKERS = {
    "s1": {"first_name": "Alice", "last_name": "Chen", "linkedin": "https://www.linkedin.com/in/alicechen-dummy"},
    "s2": {"first_name": "Bob", "last_name": "Smith", "linkedin": "https://www.linkedin.com/in/bobsmith-dummy"},
    "s3": {"first_name": "Carol", "last_name": "Davis", "linkedin": "https://www.linkedin.com/in/caroldavis-dummy"},
    "s4": {"first_name": "David", "last_name": "Wilson", "linkedin": "https://www.linkedin.com/in/davidwilson-dummy"},
    "s5": {"first_name": "Eve", "last_name": "Johnson", "linkedin": "https://www.linkedin.com/in/evejohnson-dummy"},
    "s6": {"first_name": "Frank", "last_name": "Miller", "linkedin": "https://www.linkedin.com/in/frankmiller-dummy"},
    "s7": {"first_name": "Grace", "last_name": "Lee", "linkedin": "https://www.linkedin.com/in/gracelee-dummy"},
    "s8": {"first_name": "Heidi", "last_name": "Klum", "linkedin": "https://www.linkedin.com/in/heidiklum-dummy"},
    "s9": {"first_name": "Ivan", "last_name": "Petrov", "linkedin": "https://www.linkedin.com/in/ivanpetrov-dummy"},
}

EVENTS = [
    {
        "id": 1,
        "title": "Keynote: The Future of Cloud AI",
        "speaker_ids": ["s1", "s2"],
        "category": ["AI/ML", "Keynote"],
        "description": "Kick off the day with an overview of the latest advancements in Google Cloud AI and what the future holds for intelligent applications.",
        "time": "09:00 - 10:00"
    },
    {
        "id": 2,
        "title": "Serverless Architectures on GCP",
        "speaker_ids": ["s3"],
        "category": ["Serverless", "Infrastructure"],
        "description": "Learn how to build scalable and cost-effective applications using Cloud Run and Cloud Functions.",
        "time": "10:15 - 11:00"
    },
    {
        "id": 3,
        "title": "Kubernetes Best Practices",
        "speaker_ids": ["s4", "s5"],
        "category": ["Containers", "DevOps"],
        "description": "Deep dive into GKE security, networking, and observability best practices for production workloads.",
        "time": "11:15 - 12:00"
    },
    {
        "id": 4,
        "title": "Data Engineering with BigQuery",
        "speaker_ids": ["s6"],
        "category": ["Data Analytics"],
        "description": "Unlock the power of your data with BigQuery. We will cover schema design, partitioning, and query optimization.",
        "time": "12:15 - 13:00"
    },
    {
        "id": "lunch",
        "title": "Lunch Break",
        "speaker_ids": [],
        "category": ["Break"],
        "description": "Enjoy a catered lunch and networking with fellow attendees.",
        "time": "13:00 - 14:00"
    },
    {
        "id": 5,
        "title": "Building GenAI Apps with Vertex AI",
        "speaker_ids": ["s1", "s7"],
        "category": ["AI/ML", "GenAI"],
        "description": "Hands-on session on how to leverage Vertex AI to build and deploy Generative AI applications.",
        "time": "14:00 - 14:45"
    },
    {
        "id": 6,
        "title": "Securing your Cloud Infrastructure",
        "speaker_ids": ["s8"],
        "category": ["Security"],
        "description": "A comprehensive guide to IAM, VPC Service Controls, and other security tools available in GCP.",
        "time": "15:00 - 15:45"
    },
    {
        "id": 7,
        "title": "Modern App Development with Firebase",
        "speaker_ids": ["s9"],
        "category": ["App Dev", "Mobile"],
        "description": "Accelerate your app development with Firebase's backend-as-a-service features.",
        "time": "16:00 - 16:45"
    },
    {
        "id": 8,
        "title": "Closing Remarks & Networking",
        "speaker_ids": ["s2"],
        "category": ["General"],
        "description": "Wrap up the day with key takeaways and a networking session.",
        "time": "17:00 - 17:30"
    }
]

def get_event_data():
    # Enrich events with speaker objects
    enriched_events = []
    for event in EVENTS:
        event_copy = event.copy()
        if "speaker_ids" in event:
            event_copy["speakers"] = [SPEAKERS[sid] for sid in event["speaker_ids"]]
        enriched_events.append(event_copy)
    return {
        "conference": CONFERENCE_INFO,
        "events": enriched_events
    }

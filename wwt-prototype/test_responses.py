"""
Test script to verify that different company descriptions produce different AI responses.
Run this to debug if you're getting the same response every time.
"""

import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyAsWQF-V3Z4yxn3yTkWq9pWMR0hLA157F4")

def test_gemini_responses():
    """Test that different inputs produce different outputs"""
    
    test_cases = [
        {
            "name": "E-commerce Startup",
            "description": "We're a small e-commerce startup selling sustainable fashion. We have 10,000 monthly visitors but only 2% conversion rate. We're struggling with cart abandonment and customer retention."
        },
        {
            "name": "Healthcare SaaS",
            "description": "Our healthcare SaaS platform helps hospitals manage patient records. We have 50 hospital clients but they're complaining about slow load times and difficulty integrating with their existing systems."
        },
        {
            "name": "Food Delivery App",
            "description": "We're a food delivery app competing with UberEats and DoorDash in the Midwest. Our delivery times are 15 minutes slower than competitors and our driver retention is poor."
        }
    ]
    
    model = genai.GenerativeModel(
        'gemini-2.0-flash-exp',
        generation_config={
            'temperature': 1.0,
            'top_p': 0.95,
            'top_k': 40,
            'max_output_tokens': 2048,
        }
    )
    
    print("=" * 80)
    print("TESTING GEMINI RESPONSES FOR VARIATION")
    print("=" * 80)
    
    for i, test_case in enumerate(test_cases, 1):
        prompt = f"""You are an experienced solutions consultant at a company. Analyze the following company description and provide specific, actionable insights.

Company Description:
{test_case['description']}

Based on this specific company, provide:

1. TOP 3 BUSINESS PROBLEMS
   - Identify the most critical challenges this specific company faces
   - Each problem should be 1-2 sentences
   - Be specific to their industry and situation

2. 3 DEMO IDEAS
   - Create 3 unique prototype/demo concepts tailored to solve their problems
   - Each demo should be 1-2 sentences
   - Focus on innovative, practical solutions

3. EMAIL OPENER
   - Write a personalized 2-3 sentence email opener
   - Reference specific problems from their description
   - Offer concrete help and value

Be specific and avoid generic responses. Tailor everything to THIS company's unique situation.
"""
        
        print(f"\n{'=' * 80}")
        print(f"TEST {i}: {test_case['name']}")
        print(f"{'=' * 80}")
        print(f"Input: {test_case['description']}")
        print(f"\nGenerating response...")
        
        try:
            response = model.generate_content(prompt)
            print(f"\n--- RESPONSE ---")
            print(response.text)
            print(f"\n--- END RESPONSE ---")
            
        except Exception as e:
            print(f"ERROR: {e}")
        
        print(f"{'=' * 80}\n")
    
    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("=" * 80)
    print("\nCheck if the responses above are different for each test case.")
    print("If they're all the same, there might be an API issue or caching problem.")

if __name__ == "__main__":
    test_gemini_responses()
def get_started_email_template(name, email, company, industry, message):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Get Started Inquiry</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            color: #0066cc;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #0066cc;
            margin-top: 20px;
        }}
        .contact-info {{
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .message {{
            background-color: #e6f3ff;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .next-steps {{
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
        }}
        .footer {{
            font-size: 0.8em;
            text-align: center;
            margin-top: 20px;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>New Get Started Inquiry</h1>
    
    <p>Dear Bridges DATA Services Team,</p>
    
    <p>We've received an exciting new "Get Started" inquiry through our website. Here are the details:</p>
    
    <div class="contact-info">
        <h2>Contact Information</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Company:</strong> {company}</p>
        <p><strong>Industry:</strong> {industry}</p>
    </div>
    
    <div class="message">
        <h2>Inquiry Details</h2>
        <p>{name} from {company} in the {industry} industry has expressed interest in our services. Here's their message:</p>
        <blockquote>
            {message}
        </blockquote>
    </div>
    
    <div class="next-steps">
        <h2>Next Steps</h2>
        <ol>
            <li>Review {company}'s profile and any previous interactions</li>
            <li>Research the {industry} industry to prepare relevant insights and case studies</li>
            <li>Schedule a follow-up call or meeting with {name} to discuss their specific needs</li>
            <li>Assign a team member to create a tailored proposal addressing their data challenges</li>
        </ol>
        
        <h2>Key Points to Address</h2>
        <ul>
            <li>Understand their current data infrastructure and challenges</li>
            <li>Identify potential areas for data strategy improvement</li>
            <li>Discuss relevant services (e.g., Data Modernization, BI and Analytics, AI and Machine Learning)</li>
            <li>Highlight our expertise in their industry</li>
            <li>Explain our process: Discover, Analyze, Implement, Optimize</li>
        </ul>
    </div>
    
    <p>Please ensure a prompt response to this inquiry. Let's work together to help {company} unleash their data's superpowers!</p>
    
    <p>Best regards,<br>Bridges DATA Services Auto-Notification System</p>
    
    <div class="footer">
        <p>This email was automatically generated from a website form submission. Please do not reply directly to this email. Instead, use the provided contact information to reach out to the potential client.</p>
    </div>
</body>
</html>
    """


def contact_email_template(name, email, company_url, subject, message):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Contact Form Submission</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #0066cc, #003366);
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
        }}
        .content {{
            background-color: #f8f8f8;
            padding: 20px;
            border-radius: 0 0 5px 5px;
        }}
        h1 {{
            margin: 0;
        }}
        h2 {{
            color: #0066cc;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 10px;
        }}
        .info-block {{
            background-color: white;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .info-block h3 {{
            margin-top: 0;
            color: #0066cc;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>New Contact Form Submission</h1>
    </div>
    <div class="content">
        <div class="info-block">
            <h3>Contact Information</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Company URL:</strong> <a href="{company_url}">{company_url}</a></p>
        </div>
        
        <div class="info-block">
            <h3>Message Details</h3>
            <p><strong>Subject:</strong> {subject}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
        </div>
        
        <div class="info-block">
            <h3>Next Steps</h3>
            <ol>
                <li>Review the submitted information</li>
                <li>Research the company using the provided URL</li>
                <li>Prepare a tailored response addressing their specific inquiry</li>
                <li>Follow up within 24 hours to schedule a call or provide additional information</li>
            </ol>
        </div>
    </div>
    <div class="footer">
        <p>This email was automatically generated from a contact form submission on the Bridges DATA Services website.</p>
    </div>
</body>
</html>
    """

def data_revolution_email_template(name, email, company, job_title, message):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Data Revolution Inquiry</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background-color: #0066cc;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .section {{
            margin-bottom: 20px;
            padding: 15px;
            background-color: #f8f8f8;
            border-radius: 5px;
        }}
        .section h2 {{
            color: #0066cc;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 5px;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>New Data Revolution Inquiry</h1>
    </div>
    
    <p>Dear Bridges DATA Services Admin,</p>
    
    <p>A new inquiry has been submitted through the Data Revolution form on our website. Here are the details:</p>
    
    <div class="section">
        <h2>Contact Information</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Company:</strong> {company}</p>
        <p><strong>Job Title:</strong> {job_title}</p>
    </div>
    
    <div class="section">
        <h2>Data Odyssey</h2>
        <p>{message}</p>
    </div>
    
    <div class="section">
        <h2>Next Steps</h2>
        <ol>
            <li>Review the inquirer's data challenges and aspirations.</li>
            <li>Prepare a tailored response addressing their specific needs.</li>
            <li>Schedule a follow-up call or meeting to discuss potential solutions.</li>
        </ol>
    </div>
    
    <div class="section">
        <h2>Key Strengths to Emphasize</h2>
        <ul>
            <li>Visionary solutions tailored to unique data landscapes</li>
            <li>Cutting-edge technology to propel businesses into the future</li>
            <li>Expert team of data wizards</li>
            <li>Proven track record of transforming data into actionable insights</li>
        </ul>
    </div>
    
    <p>Let's ignite their data revolution!</p>
    
    <div class="footer">
        <p>Best regards,<br>Bridges DATA Services Automated System</p>
    </div>
</body>
</html>
    """
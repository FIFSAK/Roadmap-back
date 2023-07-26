from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)

# tools = load_tools(["serpapi", "llm-math"], llm=llm)

# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


def search_links_lch(response):
    query = llm.predict(
        f"""
            Context: you will be provided with a roadmap based on it, provide links to resources where you can study the topics prescribed in the roadmap find for all topics and complete response
            Roudmap:{response}
            Answer: max_tokens=unlimited"""
    )
    # query = agent.run(response)
    print("LINKS CREATED")
    # print(query)
    return query
    
a = """Roadmap for Backend Developer:

1. Programming Languages:
   - Learn and master a server-side programming language such as Python, Java, or Node.js.
   - Understand the fundamentals of the chosen language, including data types, variables, control flow, and functions.

2. Databases:
   - Familiarize yourself with relational databases like MySQL or PostgreSQL.
   - Learn how to design and create database schemas.
   - Understand how to write efficient queries using SQL.

3. Web Development:
   - Learn HTML, CSS, and JavaScript to build user interfaces and understand how the frontend interacts with the backend.
   - Explore frontend frameworks like React or Angular to enhance your web development skills.

4. API Development:
   - Understand the basics of RESTful APIs and how to design and build them.
   - Learn about authentication and authorization mechanisms like JWT or OAuth.
   - Explore API documentation tools like Swagger or Postman.

5. Server Frameworks:
   - Choose a backend framework like Django (Python), Spring Boot (Java), or Express (Node.js).
   - Learn how to build web applications using the chosen framework.
   - Understand concepts like routing, middleware, and MVC architecture.

6. Version Control:
   - Learn Git and understand how to use it for version control.
   - Familiarize yourself with branching, merging, and resolving conflicts.

7. Testing and Debugging:
   - Learn different testing frameworks and methodologies.
   - Understand how to write unit tests and perform integration testing.
   - Master debugging techniques to identify and fix issues in your code.

8. Security:
   - Learn about common web vulnerabilities and how to prevent them.
   - Understand secure coding practices and implement them in your applications.
   - Explore tools like OWASP ZAP or Burp Suite for security testing.

9. Performance Optimization:
   - Learn techniques to optimize your code and improve application performance.
   - Understand caching mechanisms and how to use them effectively.
   - Explore tools like New Relic or Apache JMeter for performance testing.

10. Deployment and DevOps:
    - Learn about deployment strategies and how to deploy your applications to production environments.
    - Understand containerization using tools like Docker.
    - Familiarize yourself with cloud platforms like AWS or Azure.

Remember, this roadmap is just a starting point. Continuously update your skills, stay updated with new technologies, and work on real-world projects to gain hands-on experience. Good luck!"""
# print(search_links_lch(a))
# print(search_links_lch("in which team playing ronaldo"))


# Group 3: Project taxonomy and recommendations for Diversity Equity and Inclusion


## Working Group Members:


* Katrina Riehl (@kriehl)
* Madicken Munk (@munkm)
* Rafal Malanij (@elgravel)
* Jenna Swarthout Goddard (@jennaswa)
* Monica Granados (@monsauce) 
* Prabhant Singh (@prabhant)
* Tania Hernandez (@TaniaHernandez23)
* Daniel S. Katz (@danielskatz)

Emeritus Working Group Members:

* Cheuk Ting Ho

Roles: 



* Lead
    * Tania 
* Note taker(s)
    * Jenna
* Understudy Notetaker: 
    * Madicken 
* Reporter/Socializer 
    * Monica
* GitHub: https://github.com/numfocus/disc-unconference-2023-projects

# Goals

**Develop a framework as a case study for a model inclusive project**

# Topics and Categories

What are the key elements we want to have in this case study? Develop a matrix of 2 axes:



* Deconstructing what a project is (need to develop definitions for each category). _What are key parts of a **diverse **and **sustainable **project?_
    * THEMES
        * Sustainability
        * Openness
        * Diversity
        * Equity
        * Inclusion
    * CATEGORIES
        * Mission/vision
        * Stakeholders
        * Legal
            * License
            * Regulatory compliance
            * Trademarking names and logos
        * Governance
            * Leadership
            * Committees
            * Roles and responsibilities
            * Decision-making
            * Conflict resolution
            * Staffing
            * Funding and finances
            * CoC (policies, enforcement, EXISTENCE)
        * Community
            * People management
            * Engaging with users/contributors/developers/maintainers
            * Mentorship (link to mentorship group’s work)
            * Training
            * Marketing
            * Communication channels
        * Technical (Infrastructure)/Technology
            * Documentation
            * Roadmap
            * Hardware (e.g., OS)
            * Software (e.g., repo, CI/CD pipelines, quality/security measures, webhooks)
            * Access management
            * Release practices 
* Stages of project life cycle/timeline


# Next steps:

* Define language and make consistent throughout the document
* Pull out general themes that apply throughout
* Ensure recommendations truly relate back to DEI and are actionable items
* Assess how recommendations support openness/transparency and can be done in a sustainable manner
* Build out as a matrix of how recommendations apply to projects at different life stages
* Find citations/references to evaluate where diversity is missing



# Resources (from Slack)



* [https://github.com/badging/project-diversity-and-inclusion](https://github.com/badging/project-diversity-and-inclusion)
* [https://doctorow.medium.com/the-title-card-from-sumana-harihareswaras-github-talk-what-would-open-source-look-like-if-it-were-35b0360f8b89](https://doctorow.medium.com/the-title-card-from-sumana-harihareswaras-github-talk-what-would-open-source-look-like-if-it-were-35b0360f8b89)
* [https://www.jmlr.org/mloss/mloss-info.html](https://www.jmlr.org/mloss/mloss-info.html)
* [https://goblin.tools/](https://goblin.tools/) Goblin Tools: Break down to-do list items into more granular tasks


# TITLE OF OUR DOCUMENT (PARTY PARTY PARTY - Work Hard, Party Harder!)

GenOSS: **Gen**eral Guidelines for an Inclusive **OSS** Project


## Themes Appearing Throughout


## Legal Category



* License
    * Definition: A **license** is an official permission or permit to do, use, or own something as well as the document of that permission or permit.[^1]


    * Components:
        * Use of the software/tool
        * Modification of the tool
        * Sharing the tool
        * Building products on top of the tool 
        * Profiting from the use of the tool 
        * Attribution / credit 
        * Sharing of license 
    * Recommendations:
        * Use an open license from [https://choosealicense.com/appendix/](https://choosealicense.com/appendix/) which allow for reuse 
        * Try to choose a license that allows for re-mix like translation, text and data mining. For example, the CC-BY-ND license doesn’t allow for derivatives. 
* Regulatory compliance
    * Definition: Regulatory compliance is how the software, project, and community adheres to the legal constructs that govern it. The legal frameworks in which a project operates may be local, national, or international. 
    * Components:
        * Licenses of upstream software
        * National laws governing user privacy, data sharing and dissemination
        * Export control laws
    * Recommendations:
        * Be aware that regulations vary from country/region, think about how your project will work in a country/region outside where the dominant groups of the project is located
        * Consider how laws will affect major components such as data, hardware and software
        * Prioritize the data privacy of your users particularly those from marginalized groups who can be deidentified. Even data that is anonymised can reveal information particularly when there are few people from a non dominant group 
        * Be aware that your software might only be available in certain regions due to the regulatory framework of various nations/regions. This may limit your community. 
* Trademarking names and logos
    * Definition: A type of intellectual property consisting of a recognizable sign, design, or expression that identifies the project from a particular source and distinguishes them from others.[^2] A logo is a type of trademark.


    * Components:
        * Design
        * Content 
        * Copy 
    * Recommendations:
        * Consider having trademarks and logos reviewed for cultural awareness 
        * Consider that symbols are not universal and things may not translate to audiences outside of your group


## Governance Category



* Preamble
    * Example: [https://docs.openml.org/Governance/](https://docs.openml.org/Governance/)
* Roles and responsibilities
    * Definition: Any specification you make to the way somebody/group might behave in your community or if somebody/group has a position of power, what are the expectations in what you do and how you relate to the community?
    * Components:
        * Steering Committee
        * Community Manager
        * DEI Manager
        * Technical rolesClear
    * Recommendations:
        * Steering committee should not only consist of developers. Try to maximize perspectives of your individuals on the steering committee. For example, include an individual who is a user and isn’t interested in contributing code upstream. 
        * Make roles visible/transparent (and well defined) and open to everybody. This makes it easier for people to know what is expected of them and reduces the chances of people missing out on “unwritten rules” of the community. 
        * Create a DEI manager position. Consider not drawing from only marginalized groups. 
        * Consider which axes of marginalization you are considering when nominating individuals for roles in the community. When considering people for leadership roles, look at the makeup of your existing committee and choose individuals who are outside of the dominant group. 
            * Consider having an anonymous nomination system open to the community to allow people to self-nominate to reduce bias introduced by leadership nominating others
        * Create an onboarding procedure for roles in your community bring everybody to the same level of knowledge and expectations regardless of background. 
        * Have a plan for term limits, individuals rotating through different roles, and succession planning
        * Link to volunteer burnout Unconference group
    * Resources:
        * I (Jenna) like to look at the Astropy team page for inspiration: [https://www.astropy.org/team.html#astropy-team](https://www.astropy.org/team.html#astropy-team)
* Leadership
    * Definition: Management approach in which leaders help set mission, vision, and strategic goals for the project while motivating individuals within the group to successfully carry out assignments in service to those goals ([Source](https://www.snhu.edu/about-us/newsroom/business/what-is-organizational-leadership#:~:text=Organizational%20leadership%20is%20a%20management,Sofia%20Tokar))
    * Components:
        * Technical Board vs. non-technical board
        * Committees 
        * The open source leadership mindset involves thinking about: ([Source](https://www.linuxfoundation.org/resources/open-source-guides/building-leadership-in-an-open-source-community))
            * Influence, not control
            * Transparency as a means of crowd-sourcing solutions, not as exposure
            * Leading, not herding
        * Seeking community consensus is more important than being right
    * Recommendations:
        * Have a defined path to leadership for all community members
        * Have leadership reflective of your community 
        * Reflect on how the decisions you make in leadership may affect or exacerbate inequality for marginalized groups. 
        * Define expectations to remove unwritten rules and ensure that all leadership members are set up to succeed as leaders, including people from underrepresented groups in the project
        * Training DEI for leadership to raise awareness of systems of oppression 
        * Consider which axes of marginalization you are considering when nominating individuals for leadership roles. When considering people for leadership roles, look at the makeup of your existing team and choose individuals who are outside of the dominant group. 
            * Consider having an anonymous nomination system open to the community to allow people to self-nominate to reduce bias introduced by leadership nominating others
        * Step in if there is a clear violation
* Committees
    * Definition: a group of people that works together on a specific topic or question and may report to leadership with recommendations or having a specific role within the project governance. Any combination of board members, staff members, and volunteers can make up a committee. ([Source](https://www.boardeffect.com/blog/nonprofit-board-committee-structure/))
    * Components:
        * Here is a list of some of the typical board committees for nonprofit organizations ([Source](https://www.boardeffect.com/blog/nonprofit-board-committee-structure/)):
            * Executive Committee 
            * Standing Committee 
            * Ad-Hoc Committee 
            * Fundraising Committee 
            * Finance Committee 
            * Governance and Nominating Committees
            * Communications and Public Relations Committees 
            * Audit Committee 
        * Other technical project committees can also exist, such as domain-specific committees in projects like astropy or committees governing specific subsets of the project (e.g. project jupyter)
    * Recommendations:
        * Have code of conduct committee, to foster a safe space for all community members
            * Use defined best practices that support DEI, including formal training of CoC members
        * Have a defined path to committees for all community members
        * Have a clear objectives and process defined for every Committee (e.g., charters, terms of reference)
        * Communicate decision making transparently; when possible publish minutes or decision - making process publicly. 
        * Consider which axes of marginalization you are considering when nominating individuals for committees. When considering people for committee positions, look at the makeup of your existing committee and choose individuals who are outside of the dominant group. 
            * Consider having an anonymous nomination system open to the community to allow people to self-nominate to reduce bias introduced by leadership nominating others
        * Ensuring individuals, especially those belonging to an underrepresented group, do not disproportionately serve on multiple committees
* Decision-making
    * Definition: The process of making choices in a project by identifying the need for a decision, gathering information, and assessing alternative resolutions.[^3] In a project, decision making may be limited to specific groups as defined in the project governance.


    * Components:
        * Defining different types of decisions (e.g., technical vs. CoC vs. future of project, roadmap, governance)
        * Defining what method will be used to reach a decision (e.g. lazy consensus, a simple majority, a fixed percentage, unanimity)
        * What is done if a decision is not agreed upon by the decision making group  
        * Who can make decisions and how those people are chosen. 
    * Recommendations:
        * Reach decisions by consensus (perhaps lazy consensus) when possible  
        * Make and publish minutes public to promote inclusivity through transparency
        * Have processes to challenge decisions 
        * Have a process for resolution in case of decisions deadlock 
        * Ensure the decision-making process (e.g., which group/people makes the decision, how they make it, timeline) is well-defined, documented, and public, to be clear about who should be in the room to make decisions at different levels
* Conflict resolution
    * Definition: a way between two or more parties to come to agreement.
    * Components:
        * Awareness of the problem 
        * Conflict of interests 
        * What are the conflicts we are talking about?
            * Person-to-person
                * Personal conflicts/personality differences
                * Interaction with contributors
            * Technical decisions
            * Conflicts with a policy (& conflicting policies)
    * Recommendations:
        * Conflict resolution is separate from CoC violations and should be treated as such. 
        * 
* Staffing
    * Definition: The process of recruiting and hiring individuals to fill roles defined for the project, including leadership positions
    * Components:
        * Clearly define role requirements
        * Who should fill the role
        * Recruitment pipelines
        * Whether/who to pay 
        * How much to pay
        * Logistical procedures for hiring (e.g., contracts, full-time vs. part-time vs. contractors)
        * Succession planning
    * Recommendations:
        * Reach out to spaces to recruit in spaces that are underrepresented in your project. Do this in a meaningful way by building in a relationship with these groups. 
            * Be aware that this may involve a cost ($ or time) and plan for this cost
        * Leverage network to reach marginalized and non-dominant groups (e.g., events)
        * Do NOT publish pay associated with specific names!! This can put individuals at risk
            * But payment for tasks can be public
        * Have transparency in pay levels. Marginalized groups historically are paid less in positions without pay transparency. 
        * Clearly define role requirements to avoid staff over working 
        * Use tooling to check job posting for inclusive language 
    * Resources:
        * [https://about.gitlab.com/handbook/total-rewards/compensation/](https://about.gitlab.com/handbook/total-rewards/compensation/)
        * “**Diversity, Inclusion & Belonging** - People with the same attributes should earn the same. The Compensation Calculator reduces unconscious bias or giving higher pay to individuals who can negotiate better. The Compensation Calculator allows us to take a data-driven approach to compensation where there's fairness across all teams, levels and countries.”
        * “Your compensation = SF benchmark x Location Factor x Level Factor x Exchange Rate”
* Funding and finances
    * Definition: Assembling the resources needed to develop, maintain, and sustain the project, and then using them to actually do the work of the project, as determined by the project’s governance and decision-making processes.
    * Components:
        * Resources: Funding
            * Grants
            * Gifts/donations
            * Contracts
        * Resources: People
            * Volunteers (people who are not paid for their work at all)
            * Employees (people who are paid for their work by their employer, but not by the project)
        * Expenses: People
            * See staffing for people who the project pays
            * Volunteers
        * Expenses: Infrastructure
            * Technical infrastructure - see below, noting that some may have costs and some may not
                * May include physical infrastructure (must be purchased and then maintained) as well as services (can have regularly scheduled expenses)
    * Recommendations:
        * Consider the sources of resources; some may not match the projects principles and should not be accepted
        * Consider sharing proposals, perhaps and their reviews, to allow broader communities understand them and use them as examples, in order to broader the set of potential proposers
        * Consider making both the principles/processes and the decisions you make regarding projects resources (both financial and volunteer) and project resource usage (both financial and volunteer) public 
        * Consider principles of DEI in making decisions about resource allocation
        * Support the LMIC group’s work (link to outputs)
* Code of Conduct (CoC)
    * Definition: A code of conduct is a set of rules outlining the norms, rules, and responsibilities or proper practices of an individual party, project, or an organization, and the means to enforce it.
    * Components:
        * Code of Conduct document which includes defined goals, principles, policies, and processes
        * Code of Conduct committee/process
            * Reporting and Documenting Violations
                * Confidentiality
            * Inquiry / Investigation
                * Bias and Impartiality
            * Resolution
                * Checks and Balances
    * Recommendations:
        * Base a CoC document on existing documents rather than starting from scratch
        * Consider professional training for CoC members
        * CoC committee should not consist of one person or even numbers
        * Consider what information will and will not be shared, and with who, in the CoC process
    * Resources:
        * “[How to Respond to Code of Conduct Reports](https://frameshiftconsulting.com/2018/12/10/free-code-of-conduct-enforcement-book-available-now/)”, by Valerie Aurora and Mary Gardiner


## Community Engagement



* Managing people 
    * Definition: The process of training, motivating, and directing employees/staff/volunteers for progress, growth, and employee/staff/volunteer satisfaction[^4]


    * Components:
        * Training
        * Task management (could be delegation)
        * Meeting deadlines
        * Conflict resolution
        * Building culture
        * Communication
        * Recognition 
        * Growth (personal, professional) 
        * Mentorship/coaching
    * Recommendations:
        * Consider providing resources for project leadership on how to manage a diverse team 
        * Transparent task management system that allows people to state task assignments, preferences, and progress
            * Tasks can be term-limited or ongoing 
        * Make invisible work into visible tasks, if possible to recognize work of people that may be outside of traditional visible work. Many underrepresented people end up doing invisible work to support their community and this provides some equity into recognition of tasks 
            * When a person does something that they think is not currently listed as a task, they should be able to record it 
        * Be aware of your team’s personal preferences and distribute the work based on that (project is not just code!)
        * Link to volunteer burnout Unconference group
* Stakeholders
* Definition: Stakeholders can be in one or more of the following categories
        * Users
        * Contributors
    * Developers 
    * Maintainers
    * Funders/sponsors
    * External formal or informal media/communications/writers
    * Employers of any of the above categories
* Recommendations
    * Listed elsewhere in the document
* Engaging with Stakeholders 
    * Definition: how the project works with one or more categories of stakeholders (as defined above) with the goal of keeping them engaged in the project
    * Components:
        * Onboarding
        * Maintaining engagement
        * Increasing engagement
        * Planning for stakeholder turnover (when stakeholders leave, succession planning) - tied to staffing (above)
        * Recognition and attribution 
    * Recommendations: 
        * Allow individuals that performed work to represent themselves if possible. If leadership presents that work, ensure that correct attribution is given.  
        * Formal and informal reporting to funders/sponsors that include DEI aspects on the schedule that they request
        * Be time conscious, make the best use of everyone’s time. 
        * When scheduling, be aware of time zones putting people outside of working hours and be aware of religious holidays, including religions outside of the dominant group of the project.
        * Have different methods of recognition for stakeholders so that there are multiple pathways individuals can be recognized for their work and so that different stakeholders can recognize it. This helps improve visibility of work, including invisible work from non-dominant groups. 
        * Try to have stakeholders from different groups (or all stakeholders) represented on your committees and in your project leadership. 
        * Provide opportunities beyond code contribution for stakeholders to contribute to the project that match the preferences and styles of different people. 
        * Offer as many community resources in as many languages and as many accessible formats as possible
        * Link to DISCOVER cookbook
        * Link to contributor diversity tooling Unconference group
* Mentorship 
    * Definition: Guidance, or direction given to contributors by more established contributors or leadership in the service of having less experienced contributors have a successful experience and growth in the project.
    * Definition 2: A relationship between two people that helps both of them grow via regular communication. Typically one is the mentor who has particular skills and experiences, and the other is the mentee, who has a particular goal for the relationship.
    * Components:
        * Assessment
        * Timing  
        * Goals/Setting expectations
        * Informal vs. formal mentorship programs (e.g., GSoC, Outreachy)
    * Recommendations: 
        * Link to mentorship group work
        * Think about the way you recognize the stakeholders that would benefit from mentorship 
* Training
    * Definition: Teaching skills or knowledge of the components of the project in a structured manner. 
    * Components:
        * Purpose
        * Development of material 
        * Delivery 
        * Measuring results
        * Continuous education
        * Synchronous vs. asynchronous
    * Recommendations: 
        * Try to remove language barriers
        * Think about different audiences, define them and target proper level of advancement
        * Consider modes of delivery of your training when designing it. Asynchronous vs. synchronous training may require different tooling, explanations, documentation, etc. 
        * Ensure that training work isn't mostly performed by particular groups of people and that all groups have opportunities to be involved in all aspects of the project. (tied to managing people)
        * Recognize all contributors to training.
        * Have accessible tutorial templates (slides, Jupyter notebook, code) and infrastructure for trainers/instructors. 
        * Reflect on how what biases might be ingrained in your training 
* Marketing
    * Definition: The methods by which the project engages with society outside of the project community and their execution. 
    * Components:
        * Defining your audience
        * Academic and software publications
        * Conference presentations 
        * Blog posts and interviews 
        * Community alliances (e.g. participation in NumFOCUS or Scientific Python)
        * Logos and trademarks of project components (branding)
        * Events (workshops, training events)
        * Social media
        * Brand awareness
    * Recommendations: 
        * First step: Make sure that you have clearly defined your audience, and use that to guide every branding/marketing decision you make
        * Provide clear definitions on who/what get authorship and attribution, rather than having unwritten rules about it. 
        * The people who do the work should get the credit for the work, and have the opportunity to be named in the marketing (e.g., authorship, being interviewed). These decisions should be made without considering people's membership in particular groups.
        * Consider and examine what “work” you are considering valuable for attribution and recognition in your materials. 
        * Consider having external facing materials (e.g., a brand book) reviewed for cultural awareness 
        * Have images that represent the project be meaningful and accurate 
        * When using materials that are broadly disseminated, consider that symbols are not universal and things may not translate to audiences outside of your group.  
        * Consider that some social media platforms may not be accessible in certain regions (e.g., Threads in the EU)
        * Consider using accessibility features (e.g., alt-text, subtitled videos)
        * Link to DISCOVER cookbook - [https://discover-cookbook.numfocus.org/intro.html](https://discover-cookbook.numfocus.org/intro.html)


## Mission/Vision Category



* Definition: The mission and vision statements should define what the project aims to achieve, its purpose, and its target audience and where it aims to be.  \
"Project" includes the community, code, software, and governance of a project. 
* Components:
    * What are the questions that you ask?
    * Strategic goals
    * Vision statement (where the project wants to be)
* Recommendations: 
    * Consider weaving in aspects of inclusion, equity, and diversity to a mission and vision at the inception of a project or before significant growth happens ensures that the project can grow with these principles, rather than them being added later. These aspects are built into aspects of the project’s culture. 
    * Stating your project’s values explicitly and how they align with your mission and vision help reinforce and clarify your ideals of diversity and inclusion. 
    * Ensure that the group developing the mission/vision is representative not only of your stakeholder but also the stakeholders that you want to recruit including underrepresented groups


## Technical 



* Documentation
    * Definition: Documentation refers to the set of written materials accompanying a software that describes how to use it, how it works, and how it is developed and maintained. 
    * Components:
        * User docs (Installation, how to get started)
        * Developer/technical docs (API, contribution documentation)
        * Narrative documentation (tutorials, how-to guides) 
        * Release notes, changelog
        * Design docs, taxonomy and definitions
        * Terms of use
    * Recommendations
        * Translated documentation for different communities
        * Choose tooling consciously so that your documentation can be used easily by people with different accessibility tools and/or languages with unique characters
        * Try to use inclusive language in your documentation. Don’t assume unique aspects of your audience’s individuality when
        * Accessibility for people with disabilities. Eg: visualization for people with disabilities, transcripts, follow something like WCAG Guidelines [https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/)
        * Having different documentation for different audiences (beginner, advanced, expert)
        * Include links to CoC, technical standards and other relevant documents.
        * Refer to [https://www.writethedocs.org/](https://www.writethedocs.org/) 
        * Being able to compile documentation offline, with available directions on how to compile it - people in closed rooms or in the areas with very poor internet connection.
    * Resources:
        * [https://diataxis.fr/](https://diataxis.fr/)
* Project Roadmap
    * Definition: An Open Source Software (OSS) roadmap refers to a strategic plan or timeline that outlines the goals, objectives, and planned activities for the development and evolution of an open-source software project
    * Components:
        * Timeline
        * Milestones
        * Current status
        * Long term goals
        * Developer roadmap
    * Recommendations
        * Accessibility to Roadmap for OSS projects.
        * Consider biases in constructing the roadmap, pay attention to developer roadmap but as well as  a community and strategic roadmap.
        * Make sure all stakeholders are contributing to the project roadmap
* Hardware (e.g., OS)
    * Definition: Includes a physical components of a computer that the software should work on [https://en.wikipedia.org/wiki/Computer_hardware](https://en.wikipedia.org/wiki/Computer_hardware)
    * Components:
        * CPU
        * GPU
        * Physical memory
        * Operating system
        * Computer storage
        * Specific appliance
        * Operating System
        * Cloud Dependencies
    * Recommendations
        * Consider supporting major OS - Linux, Windows, MacOS (and make sure your core development team includes those who are able [and willing] to work towards this support)
        * Consider cloud vendor independence for interoperability between regions 
        * Hardware independence - supporting different platforms
        * Ensure backward compatibility
        * Consider running your software on low cost hardware.
        * Modular software with options to make sure a part of software can still run without specialized or high cost hardware. 
* Software (e.g., repo, CI/CD pipelines, quality/security measures, webhooks)
    * Definition: Set of computer programs and associated documentation and data /https://en.wikipedia.org/wiki/Software
    * Components:
        * Software dependencies
        * CI/CD
        * Software metrics
        * Testing infrastructure
        * Bootstrap scripts
        * Examples (including required input and output data when appropriate)
        * Accessibility requirements 
    * Recommendations
        * Consider not having closed source dependencies
        * Consider not being dependant on proprietary services
        * Keep old binaries accessible
        * Be cautious with metrics
        * Consider sharing metrics that demonstrate inclusion or diversity successes or challenges 
        * Create CI/CD to cover major platforms and usage scenarios (libraries)
* Data
    * Definition: All data that was required for the project - training data, example data
    * Components
        * Associated data
        * Derived data
        * Analysis
        * Data applications
    * Recommendations:
        * Be mindful of bias in data:
            * Sampling skew
            * Oversampling and boosting bias data
            * Cultural bias
            * Features relying on gender, race, geolocation etc
            * Fitting data to person worldview
            * Affirmation bias
        * Add versioning to data sources 
        * Repeatability testing
* Communication channels
    * Definition: the means by which the project and its stakeholders communicate with each other
    * Components:
        * Email (One-on-One, group mailing lists)
        * Chat tools (e.g., Slack, Discord, Rocket.Chat)
        * Developer forum (e.g., Discourse, Stack Overflow)
        * Social media
        * Newsletter
        * Source code repository files (e.g., README, CoC, Contributing)
        * Source code repository system (e.g., issues, PR discussion)
        * Traditional media (newspapers, press releases, radio/tv, etc.)
        * Blogs/videos
        * Scholarly activities (e.g., papers, talks)
    * Recommendations
        * Support asynchronous discussions to allow for diverse timezones and schedules
        * Support diverse channels to support the styles of different stakeholders
        * Use accessible channels and their features (e.g., alt text)
        * Be sure to have a plan to remain engaged and monitor communications channels so that stakeholders are "heard"
        * Develop guidelines for the project's use of channels, recognizing that community members have diverse schedules and needs that affect when and how they can use the channels (e.g., respond to messages)
        * Be certain that CoC is applied to all channels
        * Develop a welcoming and inclusive culture for use of communications channels, such as using intentional language (e.g., avoiding slang, stereotypes, abbreviations, jargon)
        * Make communications public whenever possible, for inclusiveness
* Release policies
    * Definition: The way new functionalities and product fixes are being released
    * Components:
        * Changelog
        * Trainings update
        * Documentation updates
    * Recommendations:
        * Include your community in defining a release scope
        * Include proper attribution that can be broader than just software contribution. You can include an author contribution statement defining different contributions by authors. Consider a framework similar to [CRediT](https://beta.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement?trial=true).

<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:

     https://en.wikipedia.org/wiki/License

[^2]:

     https://en.wikipedia.org/wiki/Trademark

[^3]:

     [https://www.umassd.edu/fycm/decision-making/process/#:~:text=Decision%20making%20is%20the%20process,information%2C%20and%20assessing%20alternative%20resolutions](https://www.umassd.edu/fycm/decision-making/process/#:~:text=Decision%20making%20is%20the%20process,information%2C%20and%20assessing%20alternative%20resolutions)

[^4]:

     [https://www.indeed.com/career-advice/career-development/guide-to-people-management#:~:text=People%20management%20is%20the%20process,boost%20employee%20performance%20every%20day](https://www.indeed.com/career-advice/career-development/guide-to-people-management#:~:text=People%20management%20is%20the%20process,boost%20employee%20performance%20every%20day)

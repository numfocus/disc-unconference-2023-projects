# Methodologies For Collecting Community Data

```{article-info}
:avatar: images/disc-icon.jpg
:avatar-outline: muted
:author: "[anavelyz](https://github.com/Anavelyz), [@natmokval](https://github.com/natmokval), [@akcouli](https://github.com/akcouli), [@ruv7](https://github.com/Ruv7), [@ashmpace](https://github.com/ashmpace)"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

## Introduction
This toolkit is a first draft and work in progress. It was created at the 2023 Diversity and Inclusion in Scientific Computing (DISC) Unconference.

It is provided here with the intention of sharing our work but should not be considered ready for use.

The five co-authors commit to continuing the development of this resource and welcome additional co-authors who are passionate about surveys and data analysis!


## Table of Contents
 - Definitions - Who is a contributor? Who is a user?
 - Community Survey: Satisfaction Data
 - Community Survey: Demographic Data - English version
 - Demographic Data - Translated versions
 - Demographic Data - Recommendations for administering

### Survey: Satisfaction Data

#### Introduction
Have you ever wondered how satisfied the contributors and users of your project are? Open Source (OS) communities do not have a standard mechanism for collecting feedback. We invite you to gather a new perspective and collect data with the goal of measuring satisfaction trends as a measure of the health of your project. 

The two surveys included here are designed for Open Source communities in mind. Gathering data is the best method to test assumptions and objectively measure how satisfied the community is. Satisfaction can be measured from two perspectives; the people who contribute and those who use the tool. 

What can be done with results?
 - Identify the reasons why your contributors and users are detractors of your open source project. 
 - Set goals that will increase the number of promoters of your project. 
 - Compare year over the year NPS, create dashboard (pending - can we create a dashboard)

#### Community: Targeted Respondents
CONTRIBUTORS: People who contribute to an OS project. CONTRIBUTIONS ARE NOT LIMITED TO CODE. Contributors can also be users but for the purposes of this survey we are asking them to evaluate their experience as Contributors.
 - Code contributor - a person who opens a pull request
 - Organizers/speakers for events, meetings, conferences
 - Writing, editing and updating documentation
 - UI or UX Design
 - Testing
 - Operations activities that move forward the goals of a project, such as but not limited to: project management, social media administration, communications administration, fundraising, governance

USERS: People who use software but do not contribute to it. Has used the software to perform a task in the past 12 months. 

#### Documentation: How to conduct an NPS Survey

##### Survey Checklist
- Familiarize yourself with NPS, read documentation
- Socialize the idea of using NPS among your project’s leadership to secure support or consensus for your idea including a project plan for open and close dates for the survey and a process for analyzing data
 - Create a survey in any software you prefer - see the questions below 
 - Define collection methods and where you will promote the survey
 - Invite your community to answer
 - Once you have data in hand you will need to spend some time analyzing and summarizing results
 - Share results with your community

##### What is Net Promoter Score?
The NPS assumes a subdivision of respondents into "promoters" who provide ratings of 9 or 10, "passives" who provide ratings of 7 or 8, and "detractors" who provide ratings of 6 or lower. The net promoter score results from a calculation that involves subtracting the percentage of detractors from the percentage of promoters collected by the survey item. The result of the calculation is typically expressed as an integer rather than a percentage.

[What is Net Promoter Score and When to Use It](https://chartio.com/learn/product-analytics/what-is-net-promoter-score-nps/)

[Wikipedia Article about NPS](https://en.wikipedia.org/wiki/Net_promoter_score)

##### Contributor Survey Questions
1. Are your contributions to Project X code, non code, both? 
Hypothesis - NPS for those who contribute both is higher and we can use that as a way to demonstrate the value of encouraging engineers to make non code contributions. 

2. On a scale of 0 to 10, how likely is it that you would recommend contributing to project x to a friend or colleague?

3. Please tell us more about why you provided this rating.

##### User Survey Questions
1. On a scale of 0 to 10, On a scale of 0 to 10, how likely is it that you would recommend using project x to a friend or colleague? 

2. Please tell us more about why you provided this rating.

##### How to analyze results of your survey
 - Calculate NPS (pending)
 - Manually evaluate open ended comments
 - Compare segments (for Contributors survey only)

#### Challenges
**Collecting a representative sample.** The size of an OS community can be hard to quantify therefore the percentage of response will be hard to quantify. How can we define what the target number of respondents is?

**Survey should be conducted once a year.** There is no benchmark for NPS in Open Source (that we’re aware of) Therefore the value that we propose is in comparing year over year satisfaction data. This means the survey will need to be conducted more than once in order to be valuable.

#### Next Steps
 - Collaboration will continue past the event. Anavelyz Perez and Ana Ruvalcaba will work together to continue refining the documentation. 
 - Connect with others who have expertise in NPS, if you have conducted NPS in any context or you would like to join us please open an issue.


### Survey: Demographic Data
These questions are based on questions 100-112 in the quantitative section of the NumFOCUS Contributor Diversification and Retention Research Project Baseline Survey (*link pending*).


#### English version
These questions are based on questions 100-112 in the quantitative section of the NumFOCUS Contributor Diversification and Retention Research Project Baseline Survey (*link pending*).

Here is an [English version of the survey in Google Forms](https://docs.google.com/document/d/1Lz__kuSaO2YUhRkUtxOX_KnHCi6Vyo-4j7Ftxyrg9ak/edit).

#### Translated versions
Here are preliminary versions of the survey in [French](https://docs.google.com/document/d/1i3nV7vXM0M-amqvSnICMu9u6RT_QPF2wYCThLWyIxkI/edit?usp=drive_link), [Spanish](https://docs.google.com/document/d/1FHhpfGxxddIBt_CR8mgOu20_Y0Ca42ByKUr8Zwd-PA4/edit?usp=drive_link), and [Russian](https://docs.google.com/document/d/1hGPxYZGTVLQaiXEHWXG6dFjhOB5oRTmo25sw9lRLDjs/edit?usp=drive_link). Additional translations are encouraged!

#### Recommendations for admininstering

##### For NumFOCUS
 - **Administration of a pilot version** - An initial campaign would be made to the 20 projects that participated in the CDR project, with a goal of confirming five projects who will commit to issuing the Demographic Survey to their contributor bases and provide feedback on the administration process and completion rate. 

##### For open-source projects
 - **Timing** - When first beginning to collect demographic data on the contributor base, a project should encourage as much of the existing contributor base to complete the survey. Following the initial survey, the survey should be delivered on an individual basis as part of an onboarding package to new contributors to a project, or within a certain time frame of opening a first pull request.
 - **Channel of delivery** - Project leads can send the survey questions to contributors via platforms such as Google Forms or Survey Monkey.
- **Voluntary participation** - Project leads should emphasize that completing the survey is not mandatory in order to participate as an open-source contributor. Suggested language:
>E.g of introductory statements that can be used by the project. Thank you for your time to participate in the [Survey]. [project] is collecting this data in order to guide our strategy in attracting and retaining diverse contributors. Your participation will require approximately 10 minutes. There are no known risks or discomforts associated with this survey. Your responses will be kept strictly confidential. Taking part in this study is completely voluntary, but your views are very important to us. Thank you in advance for your collaboration. Do you agree to proceed?

 - **Reminders** - To ensure a higher level of survey completion, project leads could schedule automated follow-up communications to remind contributors to complete the survey upon opening a new PR. Linking survey reminders to the opening of pull requests can help ensure that both existing and new contributors are prompted to complete the survey.

### Looking Forward: Dashboard for contributor metrics

#### Motivation
Such a tool would give project leads a greater ability to distinguish the variety of new contributors’ experience levels and how that experience maps to the project’s needs with the goal of knowing how to support new contributors and growing their community.

Project leads can use the statistical analysis available in this tool both to analyze the project’s historical progress and to plan key performance metrics for the future.

#### Metrics to consider in evaluating contributors:
 - Experienced in open-source / Inexperienced in open-source
 - Regular frequency of contribution to a single project / Irregular frequency of contribution to a single project
 - Newly joined the project / Joined the project earlier

#### Classes of contributor:
1. Experienced, regular contribution, newly joined
2. Experienced, regular contribution, joined earlier
3. Experienced, irregular contribution, newly joined
4. Experienced, irregular contribution, joined earlier
5. Inexperienced, regular contribution, newly joined
6. Inexperienced, regular contribution, joined earlier
7. Inexperienced, irregular contribution, newly joined
8. Inexperienced, irregular contribution, joined earlier

#### Challenge to data access
Currently, contributor statistics exist in GitHub, but these are publicly available on an individual project level only. This presents a challenge to analysis spanning multiple projects. For example, one individual may be a new contributor to one project, but a core maintainer of a second project, and a regular contributor to a third project. Having programmatic visibility into the entire span of many contributors’ experience across projects can help project leads/maintainers better navigate and nurture the relationships with their contributor base.

#### Recommended actions to take based on data insights
 - Provide support for beginning contributors (mentorship, skill sharing)
 - Organize sprints for beginner contributors
 - Provide support for advanced contributors (appreciation, recognition, labels or badges)
 - Provide funding support or grant opportunities
 - Invitation to join organizations, committees, opportunities for greater involvement

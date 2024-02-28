# ECON BUDGET MONEY MANAGER

The project called Econ-budget Money Manager is for helping people keep track of personal finances, each project is only accessible to the one who created it. 
The project uses a django framework, and materializecss to help make the project responsive and able to be used a multitude of devices, this project is mainly designed to be used on phones and tablet devices. This app is mainly aimed at people trying to keep track of the expenses



## Features 


### Existing Features

- __Navigation Bar__

  - This section is used for helping people log in, log out, register or create a project.
  - This links are enabled to allow the user to navigate the pages and also to, the logo is also interactable to bring you to the home page
  - I have also made the navbar responsive so its still able to be used on smaller devices

![navbar](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157708/Screenshot_43_myyufd.png)

![Nav Bar](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157708/Screenshot_42_mo6rqz.png)

![landingpage](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709158730/Screenshot_41_m1uke0.png)

- Home page

  - The home page has three different things that will appear depending on the circumstances and status of your visit using DTL(django template language)

  ![signed in](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157709/Screenshot_44_ejz2pg.png)

  ![project list](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157709/Screenshot_45_tukj3a.png)


- __Sign in Page__
![Sign in page](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157710/Screenshot_46_odvvpm.png)

  - This section will allow the user to sign in using their already created user info,  

- __Sign up page__ 

  - This section allows the user who is not a registered or authenticated user to sign up and use the site
![Sign up page](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157710/Screenshot_47_hqphlw.png)

- __Logout page__ 

- This section allows the user to sign out and it confirms with him as part of a defensive design to make the user aware of his action and choices.
![logout](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157710/Screenshot_48_m7vwtr.png)

- __The Footer__ 


  - The footer section includes links to the relevant social media sites for Econ Budget. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media

![Footer](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157710/Screenshot_49_ltqxme.png)

- __Add Project__

- This section allows users to create a project using the input fields, for name/title, cost and to add categories to this project.
- this section allows for the Create in the core of crud functionality by allowing the user to create a project which is then read from the database of the user and displayed on the home screen
- as it currently stands it is possible to create project with out a category which will cause the expense modal to break down and not function

![Add project](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157710/Screenshot_50_n47edm.png)

- __Project Detail Page__

- This section allows the user to update the expenses on each project which then modifies the cost this allows the user to Update according to crud funcitonality and makes it so the user can tell how much budget he has left
- this section also has user centric text colour to convey whether there is money left or not

![Project detail](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157710/Screenshot_52_gou7ik.png)

- __Add Expenses__
- this section shows the popup modal which has form validation the three sections allow  the  user to select a name for the expense how much it costs and the category it is assigned to.
- the project detail page will automatically update when an expense is either created or deleted
- as it currently stands a category must be assigned to the expense


![add expense](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157711/Screenshot_54_vkpgua.png)

![expense added](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157711/Screenshot_55_a1dgr4.png)
  - 

- __Delete Project__
- this section modal pops up and adds defensive programming to make sure the user is aware of his choices and when he clicks confirm it will remove the project from the database
- this fulfills the Delete in CRUD functionality
![delete project](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709159548/Screenshot_57_j17a7c.png)
### Features Left to Implement

- user email authentication, the ability to add categories to already created projects

### User Stories 

![user stories](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709161089/Screenshot_61_ya7qcu.png)
## Testing 

Through manual testing:

I first check to see if the django frame work was wired to the database and server correctly.

![test1](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157707/Screenshot_23_x4llmh.png)

![test2](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157707/Screenshot_24_pzokgl.png)

I created a simplistic view to test if the view would be shown on the server.

by clicking on the sign in button you are taken to the sign in page, if while there you do not have a registered account you can click the sign up page and you will redirected to the registration/sign up page of.
I did this through using django.allAuth

if you click add project either on the center of your screen or on the nav bar you are taken to the add project screen,
through this entire process i had Google dev tools open to check if any errors show up either on the console or problems with my code

I used a base template and extended each into the three other templates i used Project_detail, Project_list and add-project


when in the add project view you will be forced through form validation to put in a name and number, the user should be warned that it is possible to enter a negative number, this is intentional as it allows for the expenses to take it into the negative to show how much over budget they have went.

It is possible to create a project without a category but this would cause a break.

when adding categories you have to hit enter after everyone and then the categories are not only displayed their input values are then uploaded to the server via a many to one relationship one being the project many being the categories, when creating an expense in the project, the only categories able to be chosen are the categories assigned at project created 

![expense category](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709160257/Screenshot_59_ny56wq.png)

![expense category2](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709160257/Screenshot_58_nukc2l.png)


the expense form also has validation and doesnt let the user submit an invalid form, the only error message which doesnt appear is the one under the categories for add expenses, which should see one must be selected

 This project is primarily designed to be used on smaller screen sizes, with nav changing to a side nav, using materialize flex box all elements are positioned to fit on all screen sizes

 ![phone view](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709160538/Screenshot_60_kjsa0g.png)

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)(https://res.cloudinary.com/dtajxn9oi/image/upload/v1709158173/Screenshot_51_qe9wuy.png)
  ![wc3 validatorj](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709158173/Screenshot_51_qe9wuy.png)
- CSS
  - No errors were found when passing through the official [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

  ![css test](https://res.cloudinary.com/dtajxn9oi/image/upload/v1709157711/Screenshot_56_edmsxx.png)
  

### Unfixed Bugs
- the ability to create a project without a category
- The lack of form validation on the form expenses particularly the categories

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

this is a youtube tutorial which i used and adapted to suit my needs
[Youtube tutorial](https://www.youtube.com/watch?v=en4fg1F1gRs&list=PLbpAWbHbi5rNUuLTzreCl1g212G7qgzpR)

i also used a stack overflow page to add form validation to the form expenses [form](https://stackoverflow.com/questions/34999531/how-to-correctly-validate-a-modal-form)


### Content 

- all content used in this project was taken and adapted by me
- some of the pages came from and are inspired by the  I think therefore i blog code institute project

### Media

- all images were taken and uploaded by me to cloudinary to save load time on the project



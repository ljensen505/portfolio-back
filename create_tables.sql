DROP TABLE IF EXISTS `self`;
CREATE TABLE `self` (
    `id` INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `bio` TEXT NOT NULL,
    `github` VARCHAR(255) NOT NULL,
    `linkedin` VARCHAR(255) NOT NULL,
    `auth0_sub` VARCHAR(255) NOT NULL,
    `test_sub` VARCHAR(255) NOT NULL
);
INSERT INTO `self` (
        `name`,
        `email`,
        `bio`,
        `github`,
        `linkedin`,
        `auth0_sub`,
        `test_sub`
    )
VALUES (
        'Lucas Jensen',
        'lucas.p.jensen10@gmail.com',
        "I am a recent graduate from Oregon State University with a Bachelor's degree in Computer Science, driven by a passion for solving complex problems through technology. During my academic journey, I honed my skills and practical knowledge, setting a strong foundation for my career. My enthusiasm led me to a Software Engineering internship at Cvent, where I focused on Service Level Indicators (SLIs) and TypeScript. This experience allowed me to dive deep into the intricacies of backend development, gaining hands-on expertise in Python, FastAPI, Flask, Bash scripting, Linux, Nginx, and Systemd.\nMy commitment to delivering robust solutions is reflected in my proficiency in writing unit tests, ensuring the reliability and stability of the software I develop. I thrive in collaborative environments and have successfully contributed to team projects, understanding the importance of effective communication and cooperation. As I embark on my professional journey, I am excited to leverage my diverse skill set to tackle new challenges and make meaningful contributions to the field of computer science. Explore my portfolio to witness the intersection of my academic background and practical experiences that shape my identity as a dedicated and skilled computer scientist.",
        'https://github.com/ljensen505',
        'https://www.linkedin.com/in/lucas-jensen-2882aa21a/',
        'google-oauth2|103593642272149633528',
        'FZdDeArr7QuX8qVmbKD2ggdLvlJZKEjE@clients'
    );
DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects` (
    `id` INT(255) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL,
    `source` VARCHAR(255),
    `live` VARCHAR(255),
    `is_self_hosted` BOOLEAN NOT NULL
);
INSERT INTO `projects` (
        `name`,
        `description`,
        `source`,
        `live`,
        `is_self_hosted`
    )
VALUES (
        'Portfolio Backend',
        'A RESTful API for my portfolio website. Consumed by the portfolio frontend. Built with FastAPI and MySQL. Hosted on a Raspberry Pi in my living room.',
        'https://github.com/ljensen505/portfolio-back',
        'https://api.lucasjensen.me/',
        TRUE
    ),
    (
        'Portfolio Frontend',
        'The frontend for my portfolio website (this very site!). Consumes the portfolio backend. Built with React and Typescript. Hosted on a Raspberry Pi in my living room.',
        'https://github.com/ljensen505/portfolio-front',
        'https://lucasjensen.me/',
        TRUE
    ),
    (
        'Portfolio CI/CD',
        'A CI/CD pipeline for my portfolio website and used to auto build and deploy most projects listec here. Built with FastAPI and Bash, and heavily reliant upon GitHub Actions and Webhooks. Pipelines for each project vary but genarally utilize service files and systemd.',
        'https://github.com/ljensen505/portfolio-pipeline',
        NULL,
        TRUE
    ),
    (
        'Escape From Disco Love',
        'An escape room game that unfolds across three environments: a dive bar, a 1970s disco club, and an upscale rooftop bar. Players face a 30-minute time limit to break free. As they explore, a variety of interactive objects and specific items become essential tools in solving puzzles.\nBuilt with Unity and C#, Escape from Disco Love is a 3D game that can be played natively on Windows or Mac OS, or through a browser using WebGL. Built for OSU Capstone Fall 2023 with Joshua Harris, Thomas McNutt, Daniel Joseph, and Jerrod Lepper.\nSource code is private but available upon request.',
        NULL,
        'https://efdl.lucasjensen.me/',
        TRUE
    ),
    (
        'The Grapefruits Duo',
        'An artist website for a local chamber music duo. Built from scratch using Flask and sqlite. Includes a custom CMS and auth with auth0.',
        'https://github.com/ljensen505/thegrapefruitsduo',
        'https://thegrapefruitsduo.com/',
        TRUE
    ),
    (
        'Chess API',
        'A RESTful API for playing chess online. Consumed by the Chess GUI.',
        'https://github.com/ljensen505/ChessAPI',
        'https://api.chess.lucasjensen.me/',
        TRUE
    ),
    (
        'Chess',
        'A GUI for playing chess on your computer, online, against a friend. Consumes the Chess API.',
        'https://github.com/ljensen505/ChessPvP',
        NULL,
        FALSE
    )
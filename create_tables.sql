DROP TABLE IF EXISTS `self`;
CREATE TABLE `self` (
    `id` INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `bio` TEXT NOT NULL,
    `github` VARCHAR(255) NOT NULL,
    `linkedin` VARCHAR(255) NOT NULL
);
INSERT INTO `self` (`name`, `email`, `bio`, `github`, `linkedin`)
VALUES (
        'Lucas Jensen',
        'lucas.p.jensen10@gmail.com',
        'Bacon ipsum dolor amet chislic cow ball tip, drumstick pork belly tongue andouille kevin spare ribs sirloin porchetta pig sausage. Picanha filet mignon beef ribs sirloin, flank short ribs kevin swine short loin kielbasa cupim pork tenderloin bacon. Jowl ham corned beef cow. Buffalo meatloaf doner, sausage shoulder beef ribs meatball burgdoggen pancetta frankfurter prosciutto brisket chuck short ribs. Sirloin pork venison, andouille shank pancetta pork loin bacon meatloaf boudin rump. Tenderloin turducken andouille bacon.\nChislic brisket picanha chuck pork belly. Swine ham buffalo burgdoggen ribeye turkey bresaola short loin sausage salami. Tri-tip beef ribs rump, bacon turkey kevin porchetta. Corned beef bacon swine tongue cupim, bresaola strip steak short ribs brisket. Venison fatback hamburger sausage tail. Frankfurter leberkas rump hamburger meatball ground round cow spare ribs.',
        'https://github.com/ljensen505',
        'https://www.linkedin.com/in/lucas-jensen-2882aa21a/'
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
        NULL,
        'https://lucasjensen.me/',
        TRUE
    ),
    (
        'Escape From Disco Love',
        'An escape room game that unfolds across three environments: a dive bar, a 1970s disco club, and an upscale rooftop bar. Players face a 30-minute time limit to break free. As they explore, a variety of interactive objects and specific items become essential tools in solving puzzles.\nBuilt with Unity and C#, Escape from Disco Love is a 3D game that can be played natively on Windows or Mac OS, or through a browser using WebGL. Built for OSU Capstone Fall 2023 with Joshua Harris, Thomas McNutt, Daniel Joseph, and Jerrod Lepper',
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
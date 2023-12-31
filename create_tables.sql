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
    `live` VARCHAR(255)
);
INSERT INTO `projects` (`name`, `description`, `source`, `live`)
VALUES (
        'Chess',
        'A GUI for playing chess on your computer, online, against a friend. Consumes the Chess API.',
        'https://github.com/ljensen505/ChessPvP',
        NULL
    ),
    (
        'Chess API',
        'A RESTful API for playing chess online. Consumed by the Chess GUI.',
        'https://github.com/ljensen505/ChessAPI',
        'https://api.chess.lucasjensen.me/'
    )
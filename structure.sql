CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `name` varchar(255),
  `checked_in` boolean,
  `admin` boolean,
  `current_team` int,
  `current_project` int,
  `created_at` datetime
);

CREATE TABLE `tracking` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `checked_in` boolean,
  `user_id` int,
  `project_id` int,
  `timestamp` datetime
);

CREATE TABLE `project` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `teams` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

ALTER TABLE `users` ADD FOREIGN KEY (`current_team`) REFERENCES `teams` (`id`);

ALTER TABLE `users` ADD FOREIGN KEY (`current_project`) REFERENCES `project` (`id`);

ALTER TABLE `tracking` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `tracking` ADD FOREIGN KEY (`project_id`) REFERENCES `project` (`id`);

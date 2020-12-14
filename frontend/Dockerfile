FROM node:14
RUN mkdir /app
COPY ./brapifront/ /app/
WORKDIR /app
RUN npm install
EXPOSE 8080

CMD ["npm","run","serve"]

# run the app
#RUN npm install -g npm
#RUN npm install --save eslint  @vue/babel-preset-app  @vue/cli-plugin-babel @vue/cli-plugin-eslint @vue/cli-plugin-pwa vue-template-compiler@^2.0.0 vue-cli-plugin-i18n ajv@^5.0.0 chart.js@2.7.x
#RUN npm install -g @vue/cli @vue/cli-service  webpack  @vue/babel-preset-app  @vue/cli-plugin-babel @vue/cli-plugin-eslint @vue/cli-plugin-pwa  vue-template-compiler@^2.0.0 vue-cli-plugin-i18n
#RUN npm install
#RUN npm run build\
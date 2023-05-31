import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Qual é a sua idade? ", (idade: string) => {
  const idadeUsuario = parseInt(idade);

  if (idadeUsuario >= 18) {
    console.log("Você pode beber.");
  } else {
    console.log("Você não pode beber.");
  }

  rl.close();
});

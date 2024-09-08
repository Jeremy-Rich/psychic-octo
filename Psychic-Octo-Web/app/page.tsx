import Image from 'next/image';

export default function HomePage() {
  return (
    <div>
      <h1>Welcome to Psychic Octo Web (App Directory)</h1>
      <Image
        src="/coming_soon.png" // Point to the image in the public folder
        alt="Coming Soon"
        width={150}
        height={150}
      />
    </div>
  );
}